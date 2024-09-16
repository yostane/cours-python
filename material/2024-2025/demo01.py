# This is a comment
# = is an assignement
a = 10  # a is an Integer. 10 will be assigned or copied to a
b = a + 55  # Arithmeric expression
print(b)
c = 3.333  # Float
d = "Hello Python 2024"  # String -> text
e = False  # Boolean
f = True  # Boolean algebra has two values: 0/1 or False/True
print(c, d, e, f)
# Comparison expressions -> return booleans
print(a == 20, 10 > 1, "a" < "b", a >= 10, a <= 10)  # == test the equality
# and operator of the boolean algebra
print("and ->", True and True, False and False, False and True, True and False)
print("or ->", True or True, False or False, False or True, True or False)
# % modulo operator -> return the remainder of integer division
print("modulo and /", 10 % 3, 10 / 3)
# the if statement executes code conditionnaly
if a > 10:
    print("a is stricly greater than 10")
else:
    print("a is strictly less than 10")
