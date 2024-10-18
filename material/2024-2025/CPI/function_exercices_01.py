def multiply(x, y):
    """
    Ex1: Define a function that takes two arguments and returns their multiplication.
    Call this function 4 times and print the results.
    """
    return x * y


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


print(get_max(3, -8), get_max(0, 1), get_max2(1000, 100), get_max2(-7987, 333))


"""
Ex3: Define a function that takes three integer arguments and returns the smallest value.
Call this function 4 times and print the results.
"""

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

"""
Ex6: Define a function that takes an int argument. Implement the function as follows.
The function reads an interger from the keyboard (with input) and prints:
- "You win" if the entered number is bigger than the argument
- "You lose" otherwise
Call this function 1 time.
"""
