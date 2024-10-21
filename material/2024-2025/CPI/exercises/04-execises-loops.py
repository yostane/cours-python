def ex1(text):
  """Ex1: write a for loop that iterates over a string and prints only vowels (a, e, i, u, o, y)"""
  for s in text:
    if s == "a" or s == "u" or s == "i" or s == "o" or s == "y" or s == "e":
      print(s)

def ex1_2(text):
  for s in text:
    if s in "auieoy":
      print(s)

print("Exercise 1")
ex1("hello")
ex1_2("hello")

def ex2(integers):
  """Ex2: write a for loop that iterates over an array of integers and prints only mutiples of 3 or 7"""
  for n in integers:
    if n % 3 == 0 or n % 7 == 0:
      print(n)

print("Exercise 2")
print("Exercise 2 - list 1")
ex2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Exercise 2 - range(11)")
ex2(range(11))

print("Exercise 2 - range(30)")
ex2(range(30))
print("Exercise 2 - range(-12, 22, 5)")
ex2(range(-12, 22, 5))

"""Ex3: write a for loop that iterates over a string or a list and prints each character or item twice"""

"""Ex4: Given the mathematical function f(x) = x ** 5 + 3 (** means power in python),
print the value of f(x) for integers ranging from 0 to 20"""

"""Ex5: Given the mathematical function f(x) = x ** 2 + 4 x - 10,
print the value of f(x) for integers ranging from -20 to 20 (💡 you can use range(-20, 21))"""