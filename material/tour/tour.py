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

r = range(10)
print(r)

for item in r:
    print(item)

for item in range(10):
    print(item)

for i in range(10, 21, 3):
    print(i)


message = "I ♥️ Python"
for letter in message:
    print(letter)
