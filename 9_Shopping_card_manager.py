def add_item(cart):
    item = input("Enter item to add: ").strip()
    if item:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item can not be empty")

def remove_item(cart):
    item = input("Enter item to remove: ").strip()
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print("Item not found in cart.")

def print_cart(cart):
    if not cart:
        print("Cart is empty.")
    else:
        print("\n--- Shopping Cart ---")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item}")

def count_item(cart):
    print(f"Total items: {len(cart)}")


def main(): 
    cart = []

    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Count items")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            print_cart(cart)
        elif choice == "4":
            count_item(cart)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()