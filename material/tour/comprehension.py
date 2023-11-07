# Double de chaque élément
items = [0, 1, 2, 3, 4]
results = [item * 2 for item in items]
print(results)
print([item * 2 for item in items])
# puissance 4
print([item**4 for item in range(-2, 10, 2)])

# Garder uniquement les éléments pairs
items = [9, 22, -2, 11, 1232, 2323]
print([item for item in items if item % 2 == 0])

results = []
for item in items:
    if item % 2 == 0:
        results.append(item)
print(results)

# Garder uniquement les éléments pairs et les multiplier par 3
print([item * 3 for item in items if item % 2 == 0])

messages = ["Hello", "J'aime", "Python"]
print([len(message) for message in messages])
print([message + "." for message in messages])
print({message: len(message) for message in messages})
print({len(message) for message in messages})
