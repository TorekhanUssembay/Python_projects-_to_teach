class User:
    system_name = "Internal portal"

    def __init__(self, username: str):
        self.username = username
        self.permissions = []

    def show_permissions(self):
        return self.permissions

    def add_permission(self, perm: str):
        if perm not in self.permissions:
            self.permissions.append(perm)
    
    def can(self, action: str) -> bool:
        return action in self.permissions

    def __str__(self):
        return f"{self.username} ({self.__class__.__name__})"


class Admin(User):
    def __init__(self, username: str):
        super().__init__(username)
        self.permissions = ["read", "write", "delete", "modify"]

    def show_permissions(self):
        return f"Admin Permissions: {', '.join(self.permissions)}"


class RegularUser(User):
    def __init__(self, username:str):
        super().__init__(username)

        self.permissions = ["read"]

    def show_permissions(self):
        return f"User Permissions: {', '.join(self.permissions)}"

def main():
    admin = Admin("Alice")
    user = RegularUser("Bob")

    print(f"System name: {User.system_name}\n")

    print(admin)
    print(admin.show_permissions())
    print("Can delete?", admin.can("delete"))
    print()

    print(user)
    print(user.show_permissions())
    print("Can delete?", user.can("delete"))

    user.add_permission("write")
    print(user.show_permissions())
    print("Can write?", user.can("write"))



if __name__ == "__main__":
    main()