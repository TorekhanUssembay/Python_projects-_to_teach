def word_frequency(text):
    text = text.lower() 
    words = text.split()  
    freq = {}

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word:  
            freq[word] = freq.get(word, 0) + 1

    return freq


def main():
    text = input("Enter your text: ")
    counts = word_frequency(text)

    print("\nWord frequencies:")
    for word, count in counts.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
