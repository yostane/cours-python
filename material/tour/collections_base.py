# List: éléments ordonnées. Chauqe élément est défini par sont indice
numbers = [3, 4, -3, "hello", True, 390]
print(numbers)
print(numbers[0], numbers[-1], numbers[-2])

print(numbers[0:3], numbers[:3], numbers[1:5])
print(numbers[-3:-1])

for number in numbers:
    print(number)

# Dictionnaires: élements identidifiés par une clé (on parle aussi de couples clé/valeur)
pokemon1 = {"name": "Pikachu", "hp": 10, "type": "Thunder"}
print(pokemon1, pokemon1["name"], pokemon1["type"])

for key, value in pokemon1.items():
    print(key, value)

# Set (ensemble) : élements non ordonnées et uniques
messages = {"hello", "world", 2023}
print(messages, "hello" in messages, 2024 in messages)
messages.add(2023)
print(messages)

for message in messages:
    print(message)

# Tuple : éléments ordonnées immutable (on ne peut ajouter ou supprimer d'éléments). On peut le considérer comme une liste immutable
