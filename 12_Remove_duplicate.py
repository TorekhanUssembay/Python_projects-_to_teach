def remove_duplicates(data):
    seen = set()
    cleaned = []

    for item in data:
        if item not in seen:
            cleaned.append(item)
            seen.add(item)

    return cleaned

def main():
    raw_input_data = input("Enter items separated by space: ")

    original = raw_input_data.split()

    cleaned = remove_duplicates(original)

    print("\nBefore:", original)
    print("After :", cleaned)

if __name__ == "__main__":
    main()