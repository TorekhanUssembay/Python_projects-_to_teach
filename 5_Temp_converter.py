def get_number():
    while True:
        try:
            return float(input("Insert temperature, please:"))
        except ValueError:
            print("You need to insert number")

def get_value():
    while True:
        user_temp_value = input("Please insert C or F: ").upper()
        if user_temp_value not in ("C", "F"):
            print("Please insert right value")
        return user_temp_value

def convert(number, value):
    if value == "C":
        return number * 1.8 + 32
    else:
        return (number - 32) / 1.8

    return

def main():
    number = get_number()
    value = get_value()

    converted = convert(number, value)

    if value == "C":
        print(f"{number}°C = {converted:.2f}°F")
    else:
        print(f"{number}°F = {converted:.2f}°C")

if __name__ == "__main__":
    main()