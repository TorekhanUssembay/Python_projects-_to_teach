def check_permissions(user_roles, required_permissions):
    user_roles = set(user_roles)
    required_permissions = set(required_permissions)

    common = user_roles & required_permissions

    missing = required_permissions - user_roles

    return common, missing


def main():
    user_roles = input("Enter user roles separated by space: ").split()
    
    required_permissions = input("Enter required permissions separated by space: ").split()
    
    common, missing = check_permissions(user_roles, required_permissions)

    print("Permissions user has:", common)
    if missing:
        print("Missing permissions:", missing)
    else:
        print("User has all required permissions ")


if __name__ == "__main__":
    main()
