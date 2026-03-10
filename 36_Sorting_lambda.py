users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_users_by_age = sorted(users, key=lambda user: user["age"])
print(sorted_users_by_age)

sorted_users_by_name = sorted(users, key=lambda user: user["name"])
print(sorted_users_by_name)

sorted_by_age_des_by_name_as = sorted(users, key=lambda user: (-user["age"], user["name"]))
print(sorted_by_age_des_by_name_as)

