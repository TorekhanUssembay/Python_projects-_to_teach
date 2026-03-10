data = [1, 2, "3", 4, 5.0, 6]


integers = list(filter(lambda x: isinstance(x, int), data))

even_integers = list(filter(lambda x: x % 2 == 0, integers))

print(integers)
print(even_integers)

