def sort_sata(data: list, field: str, reverse=False):

    if not data:
        return data

    if field not in data[0]:
        raise ValueError(f"Invalid field: '{field}' not found in data")

    return sorted(data, key=lambda item: item[field], reverse=reverse)

users = [
    {"name": "Alice", "age": 25},
    {"name": "John", "age": 14},
    {"name": "Sam", "age": 32},
]

print(sort_sata(users, "age"))
print()

print(sort_sata(users, "name"))
print()

print(sort_sata(users, "age", reverse=True))
print()

"""
    def sort_data(data: list, field: str, reverse=False):
    Accept list of dicts
    Sort dynamically using lambda
    Raise error if field invalid
"""