from typing import Any, Optional, Iterable

def get_valid_input(
    prompt: str,
    expected_type: type, 
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    allowed_values: Optional[Iterable[Any]] = None,
):
    
    while True:
        raw_input_value = input(prompt).strip()

        if not raw_input_value:
            print("Input can not be empty")
            continue
        
        try: 
            if expected_type is int:
                value = int(raw_input_value)
            elif expected_type is float:
                value = float(raw_input_value)
            elif expected_type is str:
                value = raw_input_value
            else:
                print("Unsupported type provided.")
                continue
        except ValueError:
            print("Input must be of type {expected_type.__name__}.")
            continue

        if expected_type in (int, float):
            if min_value is not None and value < min_value:
                print(f"Input must be >= {min_value}")
                continue
            if max_value is not None and value < max_value:
                print(f"Input must be <= {max_value}")
                continue

        if allowed_values is not None:
            if value not in allowed_values:
                print(f"Value must be one of {list(allowed_values)}.")
                continue
        
        return value
    
def main():
    print("=== User Registration CLI ===\n")

    age = get_valid_input(
        prompt = "Enter age (18-65): ",
        expected_type = int, 
        min_value = 18,
        max_value = 65,
    )

    salary = get_valid_input(
        prompt = "Enter salary (>0): ", 
        expected_type = float, 
        min_value = 0.01
    )

    role = get_valid_input(
        prompt = "Enter role (admin/user/manager): ",
        expected_type = str,
        allowed_values = ["admin", "user", "manager"]
    )


    print("\n✅ Registration Successful!")
    print(f"Age   : {age}")
    print(f"Salary: {salary}")
    print(f"Role  : {role}")

if __name__ == "__main__":
    main()

