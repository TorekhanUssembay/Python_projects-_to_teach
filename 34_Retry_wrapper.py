import time
import random
from functools import wraps

def retry(max_attempt=3, delay=1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range (1, max_attempt + 1):

                try:
                    print(f"Attempt {attempt}")
                    return func(*ards, **kwargs)
                
                except Exception as e:
                    if attempt == max_attempt:
                        raise
                    
                    sleep_time = delay * (2 ** (attempt - 1))
                    print(f"Retrying in {sleep_time} seconds...")

                    time.sleep(sleep_time)
        return wrapper

    return decorator