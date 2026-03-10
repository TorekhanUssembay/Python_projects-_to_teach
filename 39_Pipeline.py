transactions = [
    {"amount": 100, "status": "completed"},
    {"amount": 50, "status": "failed"},
    {"amount": 200, "status": "completed"},
    {"amount": 80, "status": "pending"},
    {"amount": 150, "status": "completed"}
]


def main():

    completed_transactions = filter(
        lambda tx: tx["status"] == "completed",
        transactions
    )

    amounts = map(
        lambda tx: tx["amount"],
        completed_transactions
    )

    taxed_amounts = map(
        lambda amount: amount * 1.10,
        amounts
    )

    total_revenue = sum(taxed_amounts)

    print("Total revenue with tax:", total_revenue)


if __name__ == "__main__":
    main()