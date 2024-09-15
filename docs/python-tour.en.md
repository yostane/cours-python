---
title: Tour of the Language
---

# Tour of the Python Language

We will take a tour of the Python language without necessarily covering everything because it is very rich in features.

!!! warning

    As the Python language frequently evolves with improvements and simplifications, it is possible that the code examples seen here are different from what you find in the literature.

## Getting Started

- Open VSCode in an empty folder
- Create a file **hello.py** containing `print("Hello")`
- Run the command `python hello.py`
- A bit of code to get an idea of the language

```py
--8<--
tour.py
--8<--
```

## Some Characteristics

- Python is dynamically typed: a variable can change type during its use (unlike statically typed languages)
- Python is strongly typed: each data has a type and does not change implicitly
- Python supports object-oriented and functional programming
- Indentations are used to define code blocks (instead of `{}` braces commonly found in other languages)
    - The size of the indentation must be consistent within the same block
    - It is recommended to have an indentation of 4 spaces
- There are several programming conventions but they have many common points. The official convention is called [PEP 8](https://peps.python.org/pep-0008/). Here are some rules and recommendations:
    - Snake case for functions. E.g., `find_student()`
    - Use spaces to define indentation and avoid using the **tab** key

## Basic Types and Operations

- Integer (int), real (float), and complex (complex) numbers
- Strings
- Boolean values and boolean operators `and`, `or`, and `not`
- Comparison operators `>`, `<`, ... that return a boolean
    - `is` allows testing the identity between two objects. Its result can be customized.
    - `==` is sometimes equivalent to `is`
- Since Python is strongly typed, converting a value to another type must be done explicitly using `int()`, `float()`, `complex()`, `str()`, ...
