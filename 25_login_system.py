def login_system():
    correct_username = "admin"
    correct_password = "12345"

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == correct_username and password == correct_password:
        print("Login successful")
    else:
        print("Login failed")


def main():
    login_system()


if __name__ == "__main__":
    main()
