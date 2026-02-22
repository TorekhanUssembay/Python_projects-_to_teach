def add_product(inventory):
    product = input("Enter product name: ").strip()
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be an integer.")
        return

    if product in inventory:
        inventory[product] += quantity
        print(f"Updated {product} quantity to {inventory[product]}")
    else:
        inventory[product] = quantity
        print(f"Added new product {product} with quantity {quantity}")


def check_availability(inventory):
    product = input("Enter product to check: ").strip()
    quantity = inventory.get(product)
    if quantity is None:
        print(f"{product} does not exist in inventory.")
    elif quantity > 0:
        print(f"{product} is available: {quantity} in stock")
    else:
        print(f"{product} is out of stock")


def main():
    inventory = {}

    while True:
        print("\nInventory Menu:")
        print("1. Add/update product")
        print("2. Check availability")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            check_availability(inventory)
        elif choice == "3":
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
