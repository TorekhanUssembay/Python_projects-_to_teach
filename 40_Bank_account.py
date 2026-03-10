class BankAccount:
    def __init__(self, initial_balance: float = 0):
        if initial_balance < 0:
            raise ValueError("Innitial balance can not be negative")

        self.__balance = initial_balance

    def deposite(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposite amount can not be negative")

        self.__balance += amount
        print(f"Deposited: {amount}")    

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
        print(f"Withdrawn: {amount}")
    def get_balance(self) -> float:
        return self.__balance

def main():
    account = BankAccount(100)

    print("Initial balance: ", account.get_balance)

    account.deposite(50)
    print("Initial balance: ", account.get_balance)
    
    account.withdraw(75)
    print("Initial balance: ", account.get_balance)

    try:
        account.withdraw(1500)
    except ValueError as e:
        print("Error", e)

if __name__ == "__main__":
    main()