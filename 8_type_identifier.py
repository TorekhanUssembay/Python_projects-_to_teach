def detect_type(value):

    if value.lower() in ("true", "false"):
        return "Boolean", f"Logical value ({value.title()})"

    try:
        int_value = int(value)
        return "Integer", f"Whole number ({int_value})"
    except ValueError:
        pass

    try:
        float_value = float(value)
        return "Float", f"Decimal number ({float_value})"
    except ValueError:
        pass

    if value.startswith("[") and value.endswith("]"):
        return "List", "Sequence structure"

    return "String", f"Text data ({value})"


def main():
    user_input = input("Enter any value: ")

    data_type, description = detect_type(user_input)

    print("\n--- DATA TYPE REPORT ---")
    print("Detected Type:", data_type)
    print("Description:", description)


if __name__ == "__main__":
    main()
