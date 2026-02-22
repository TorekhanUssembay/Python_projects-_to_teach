def get_scores():
    scores = []

    while True:
        try:
            score = input("Enter score (or type 'done' to finish): ")

            if score.lower() == "done":
                break

            score = float(score)

            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    return scores


def calculate_average(scores):
    return sum(scores) / len(scores)


def analyze_scores(scores):
    average = calculate_average(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest


def main():
    scores = get_scores()

    if not scores:
        print("No scores entered.")
        return

    average, highest, lowest = analyze_scores(scores)

    print("\n--- Student Score Analysis ---")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


if __name__ == "__main__":
    main()