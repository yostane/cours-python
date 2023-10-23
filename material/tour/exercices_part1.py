print([1, 2, 3] * 3)
print("hello" * 2)
print(len([1, 2, 3]), len([1, 2, 3] * 3), len("hello"))


# abcdefghij
# ligne 0 -> a on prend la sous-chaine (0, 1)
# ligne 1 -> bc (1, 3)
# ligne 2 -> def (3, 6)
# ligne 3 -> ghij (6, 10)
# ligne l -> (indice courant dans la chaine, indice courant + l + 1)
# indice courant s'incrémente à chaque fois de l + 1


def print_pyramide(input):
    i = 0
    current_line = 0
    while i + current_line + 1 < len(input):
        print(input[i : i + current_line + 1])
        i += current_line + 1
        current_line += 1


print_pyramide("abcdefghij")
print_pyramide("abcdefghijklmnopqrstuvwxyz")
print_pyramide("abcdefghijklmnopqrstuvwxyz" * 10)


def count_letters1(input):
    dict = {}
    for letter in input:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def count_letters2(input):
    dict = {}
    for letter in input:
        dict[letter] = dict.get(letter, 0) + 1
    return dict


def count_letters3(input):
    dict = {}
    for letter in input:
        dict[letter] = dict[letter] + 1 if letter in dict else 1
    return dict


print(count_letters1("hello"))
print(count_letters2("hello"))
print(count_letters3("hello"))
