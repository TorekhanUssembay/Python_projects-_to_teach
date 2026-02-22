APP_NAME = "Expense Tracker"
VERSION = "1.0.0"
DEBUG = True

def print_banner():
    print("=" * 40)
    print(f"{APP_NAME}")
    print(f"Version: {VERSION}")

    if DEBUG:
        print("DEBUG IS ENABLED")
    
    print("=" * 40)

def main():
    print_banner()
    print("Application started...")

if __name__ == "__main__":
    main()