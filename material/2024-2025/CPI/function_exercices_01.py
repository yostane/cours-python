def multiply(x, y):
    """
    Ex1: Define a function that takes two arguments and returns their multiplication.
    Call this function 4 times and print the results.
    """
    return x * y


print("Exercice 1")
a1 = multiply(2, 4)
a2 = multiply(1, 0)
a3 = multiply(1, -7)
a4 = multiply(10, 99)
print(a1, a2, a3, a4)


def get_max(x, y):
    """
    Ex2: Define a function that takes two integer arguments and returns the biggest value.
    Call this function 4 times and print the results.
    """
    if x >= y:
        return x
    else:
        return y


def get_max2(x, y):
    return x if x >= y else y


print("Exercice 2")
print(get_max(3, -8), get_max(0, 1), get_max2(1000, 100), get_max2(-7987, 333))


def get_min_three(a, b, c):
    """
    Ex3: Define a function that takes three integer arguments and returns the smallest value.
    Call this function 4 times and print the results.
    """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


print("Exercice 3")
print(
    get_min_three(0, 1, 2),
    get_min_three(10, -3, 99),
    get_min_three(85, 12, 21),
    get_min_three(7, 11, -2),
)

"""
Ex4: Define a function that takes three arguments: an int and two strings.
if the first argument is even, the function returns the first string argument.
Otherwise, it returns the second string argument.
Call this function 4 times and print the results.
"""

"""
Ex5: Define a function that takes an int argument. Implement the function as follows.
The function reads an interger from the keyboard (with input) and prints:
- "You win" if the entered number is bigger than the argument
- "You lose" otherwise
Call this function 1 time.
"""
