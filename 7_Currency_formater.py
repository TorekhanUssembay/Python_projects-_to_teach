def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:,.2f}"


def main():
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    formatted = format_currency(amount)
    print("Formatted amount:", formatted)


if __name__ == "__main__":
    main()
