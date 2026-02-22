from collections import namedtuple

User = namedtuple("User", ["name", "age", "email"])

user1 = User(name="John Doe", age=29, email="john@example.com")

print(user1.name)  
print(user1.age)   
print(user1.email)  
