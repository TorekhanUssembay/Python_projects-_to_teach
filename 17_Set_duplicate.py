def deduplicate_tags(tags):
    seen = set()
    clean_tags = []

    for tag in tags:
        if tag not in seen:
            clean_tags.append(tag)
            seen.add(tag)

    return clean_tags


def main():
    raw_input_data = input("Enter tags separated by space: ")
    tags = raw_input_data.split() 

    clean_tags = deduplicate_tags(tags)

    print("Original tags:", tags)
    print("Cleaned tags:", clean_tags)


if __name__ == "__main__":
    main()
