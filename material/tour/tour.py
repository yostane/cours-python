a = 10
print(a)
a = "hello"
print(a)

b = 10
c = a + str(b)
print("a+b", c)

if b == 10:
    print(b)
else:
    print("b différent de 10")


def add(x, y):
    return x + y


print(add(-810, b))

# List
numbers = [3, 4, -3, "hello", True, 390]
print(numbers)
print(numbers[0], numbers[-1], numbers[-2])

print(numbers[0:3], numbers[:3], numbers[1:5])
print(numbers[-3:-1])

# Dictionnary
pokemon1 = {"name": "Pikachu", "hp": 10, "type": "Thunder"}
print(pokemon1, pokemon1["name"], pokemon1["type"])

# Set
messages = {"hello", "world", 2023}
print(messages, "hello" in messages, 2024 in messages)
messages.add(2023)
print(messages)

r = range(10)
print(r)

for item in r:
    print(item)

for item in range(10):
    print(item)

for number in numbers:
    print(number)

for key, value in pokemon1.items():
    print(key, value)

for message in messages:
    print(message)
