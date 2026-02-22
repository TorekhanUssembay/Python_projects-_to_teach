def check_access(role, action, permissions):
    allowed_actions = permissions.get(role, [])
    if action in allowed_actions:
        return True
    else:
        return False


def main():
    permissions = {
        "admin": ["create", "read", "update", "delete"],
        "editor": ["read", "update"],
        "viewer": ["read"]
    }

    role = input("Enter your role (admin/editor/viewer): ").strip().lower()
    action = input("Enter action you want to perform (create/read/update/delete): ").strip().lower()

    if check_access(role, action, permissions):
        print(f"Access granted — {role} can perform {action}")
    else:
        print(f"Access denied — {role} cannot perform {action}")


if __name__ == "__main__":
    main()
