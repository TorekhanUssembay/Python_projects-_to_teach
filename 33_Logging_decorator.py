import time
from functools import wraps
from typing import Callable, Any

def log_execution(func: Callable) -> Callable:
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()

        print(f"\n[LOG] Executing: {func.__name__}")
        print(f"[LOG] Args: {args}")
        print(f"[LOG] Kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"[LOG] Exception in {func.__name__}: {e}")
            raise

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"[LOG] Returned: {result}")
        print(f"[LOG] Execution Time: {execution_time:.6f} seconds")

        return result
    
    return wrapper


@log_execution
def calculator(a: float, b: float, operation: str = "add") -> float:
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        raise ValueError("Invalid operation")
    
@log_execution
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

@log_execution
def greet(name: str, uppercase: bool = False) -> str:
    message = f"Hello, {name}"
    return message.upper() if uppercase else message


