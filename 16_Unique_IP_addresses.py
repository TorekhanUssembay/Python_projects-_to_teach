def main():
    unique_visitors = set()

    while True:
        ip = input("Enter visitor IP (or type 'done' to finish): ").strip()
        if ip.lower() == "done":
            break
        unique_visitors.add(ip)

    print(f"Total unique visitors: {len(unique_visitors)}")
    print("Unique IPs:", unique_visitors)


if __name__ == "__main__":
    main()
