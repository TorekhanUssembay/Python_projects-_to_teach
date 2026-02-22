def compute_similarity(user1_interests, user2_interests):
    set1 = set(user1_interests)
    set2 = set(user2_interests)

    intersection = set1 & set2   
    union = set1 | set2          

    if not union:
        return 0 

    similarity_ratio = (len(intersection) / len(union)) * 100
    return similarity_ratio


def main():
    user1 = input("Enter interests for User 1 (space-separated): ").split()
    user2 = input("Enter interests for User 2 (space-separated): ").split()

    similarity = compute_similarity(user1, user2)

    print(f"Similarity ratio: {similarity:.2f}%")
    

if __name__ == "__main__":
    main()
