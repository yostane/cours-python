a = 10
b = "Hello"
c = True
print(type(a), type(b), type(c))

if a % 2 == 0:
    print("even")


if a % 2 == 0:
    print("A is even here")


# A function avoids repeating the same code
def is_even():
    if a % 2 == 0:
        return True
    else:
        return False


if is_even():
    print("a is even")
else:
    print("a is odd")
