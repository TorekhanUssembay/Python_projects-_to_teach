def atm():
    balance = 1000

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select option (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid option. Please select 1-4.")
            continue

        if choice == "1":
            print(f"Current Balance: ${balance}")

        elif choice == "2":
            while True:
                try:
                    amount = float(input("Enter deposit amount: "))
                    if amount > 0:
                        balance += amount
                        print("Deposit successful.")
                        break
                    else:
                        print("Amount must be positive.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        elif choice == "3":
            while True:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    if amount <= 0:
                        print("Amount must be positive.")
                    elif amount > balance:
                        print("Insufficient funds.")
                    else:
                        balance -= amount
                        print("Withdrawal successful.")
                        break
                except ValueError:
                    print("Invalid input. Enter a number.")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

def main():
    atm()


if __name__ == "__main__":
    main()
