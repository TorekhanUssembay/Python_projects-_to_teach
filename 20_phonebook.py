def add_contact(phonebook):
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()

    if not name or not number:
        print("Name and number cannot be empty.")
        return

    if name in phonebook:
        print(f"{name} already exists. Updating number.")
    phonebook[name] = number
    print(f"Contact {name} added/updated successfully.")


def search_contact(phonebook):
    name = input("Enter name to search: ").strip()
    number = phonebook.get(name)
    if number:
        print(f"{name}: {number}")
    else:
        print(f"No contact found for {name}.")


def main():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
