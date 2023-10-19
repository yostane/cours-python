# Tour du langage Python

Nous allons faire un tour du langage Python sans forcément tout couvrir car il est très riche en fonctionnalités.

!!! warning

    Comme le langage Python évolue apporte fréquemment des amélioration et simplifications, il se peut que les exemples de code vues ici soient différents de ce que vous trouvez dans la littérature.

## Premiers pas

- Ouvrir VSCode dans un dossier vierge
- Créer un fichier **hello.py** contenant `print("Hello")`
- Lancer la commande `python hello.py`
- Un peu de code pour avoir une idée du langage

```py
--8<--
tour.py
--8<--
```

## Quelques caractéristiques

- Python est dynamiquement typé: une variable peut changer de type durant son utilisation (contraire de statiquement typé)
- Python est fortement typé: chaque donnée a un type et ne change pas de façon implicite
- Python supporte la programmation orienté objet et fonctionnelle
- Il existe plusieurs conventions de programmation mais qui on beaucoup de points communs. La convention officielle est appelée [pep 8](https://peps.python.org/pep-0008/). Voici quelques règles et recommandations:
    - snake case pour les fonctions. Ex. `find_student()`
    - Utiliser des espaces pour définir l'indentation et éviter d'utiliser la touche **tab**

## Types et opérations de base

- Nombres entier (int), réel (float) et complexes (complex)
- Chaines de caractères (String)
- Valeurs booléennes et opérateurs booléens `and`, `or` et `not`
- Opérateurs de comparaison `>`, `<`, ... qui retournent un booléen
    - `is` permet de tester l'identité entre deux objects. Son résultat peut être personnalisé.
    - `==` est parfois équivalent à `is`
- Comme python est fortement type, convertir un valeur vers un autre type devra se faire explicitement `int()`, `float()`, `complex()`, `str()`, ...

## Programmation fonctionnelle

- Les fonctions sont des éléments de première classe : Les fonctions sont comme des variables
- Utilisation intensive de fonctions pures: fonction sans effet de bord, toujours le même résultat pour les mêmes entrées
    - exemples de fonctions par pure: print (car elle change la console)
- Immutabilité
    - On ne peut pas changer la valeur d'une variable une fois initialisée
    - On ne peut pas changer les propriétés d'un object une fois instancié
    - On ne peut pas ajouter ou supprimer des éléments d'une collection
- On le code est développé sous forme d'une chaîne de traitements (comme dans une usine)

## Relation entre la POO et la programmation fonctionnelle

- La POO est la prog. fonctionnelle ne sont pas mutuellement exclusifs
- On peut développer en POO avec un style fonctionnelle:
    - Les méthodes ne font pas de mutation de champs de l'objet
    - Les propriétés sont uniquement en read-only
    - Les `records` simplifient la création de ce genre de classes
