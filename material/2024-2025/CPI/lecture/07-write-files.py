# Data that we want to write to the file
# Each element of the list should end with \n 
# except for the last one 
# (otherwise the text will be in the same line in the file)
words = ["Hello\n", "world\n"]

# open("file") or open("file", "r") opens in read only mode (lecture seule in frech)
# "w" allows to create and write files
# If "w" is not specified, we cannot create or write into the file
f = open("story.txt", "w")
f.writelines(words)
f.close()

numbers = [1, 2, 3]
f = open("numbers.txt", "w")
# Python cannot write numbers into a file
# We need to convert them first into strings using str()

# The numbers will be on the same line with this solution
# Because there is not \n (new line character) at the end of each
numbers_as_strings = [str(numbers[0]), str(numbers[1]), str(numbers[2])]
f.writelines(numbers_as_strings)
f.close()


f = open("numbers2.txt", "w")
# Add a new line after each number except for the last one
numbers_as_strings2 = [
    str(numbers[0]),
    "\n",
    str(numbers[1]),
    "\n",
    str(numbers[2])
    ]
f.writelines(numbers_as_strings2)
f.close()

# With a for loop so that it works with any list size
numbers = [1, 2, 3]
f = open("numbers3.txt", "w")
numbers_as_strings3 = []
for n in numbers:
    # "append" adds an element to the end of the list
    numbers_as_strings3.append(str(n))
    numbers_as_strings3.append("\n")

f.writelines(numbers_as_strings3)
f.close()