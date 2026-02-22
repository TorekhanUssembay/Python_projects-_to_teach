def get_amounts():
    last_5_expences = []
    while len(last_5_expences) < 5:
        try:
            amount = int(input(f"You expense {len(last_5_expences) + 1}: "))
            if amount >= 0:
                last_5_expences.append(amount)
            else:
                print("Amount should be non negative!")
        except ValueError:
            print("Please enter a valid number!")
    
    return last_5_expences


def total(expenses):
    return sum(expenses)
    

def average_amount(expenses):
    return sum(expenses) / len(expenses)

def main():
    expenses = get_amounts()
    total_amount = total(expenses)
    average = average_amount(expenses)
    print(f"\n----------------\nAverage spending is: {average} \nTotal spending is: {total_amount}")

if __name__ == "__main__":
    main()