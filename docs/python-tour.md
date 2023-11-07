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
- Les indentations sont utilisées pour définir les blocs de code (au lieu des `{}` accolades qu'on trouve usuellement dans d'autres langages)
    - La taille de l'indentation doit être consistance au sein du même block
    - Il est recommandé d'avoir une indentation de 4 espaces
- Il existe plusieurs conventions de programmation mais qui on beaucoup de points communs. La convention officielle est appelée [pep 8](https://peps.python.org/pep-0008/). Voici quelques règles et recommandations:
    - Snake case pour les fonctions. Ex. `find_student()`
    - Utiliser des espaces pour définir l'indentation et éviter d'utiliser la touche **tab**

## Types et opérations de base

- Nombres entier (int), réel (float) et complexes (complex)
- Chaines de caractères (String)
- Valeurs booléennes et opérateurs booléens `and`, `or` et `not`
- Opérateurs de comparaison `>`, `<`, ... qui retournent un booléen
    - `is` permet de tester l'identité entre deux objets. Son résultat peut être personnalisé.
    - `==` est parfois équivalent à `is`
- Comme python est fortement type, convertir un valeur vers un autre type devra se faire explicitement `int()`, `float()`, `complex()`, `str()`, ...

## Collections standards

- Collection: type (ou structure) de données qui permet de gérer un ensemble de données
- Python propose plusieurs types intégrés de collections
- Voici les 4 types les plus usuels: *list*, *dict*, *set* et *tuple*

```py
--8<--
collections_base.py
--8<--
```

## La compréhension des listes, dictionnaires et ensembles

- Permet de créer une nouvelle liste, dictionnaire ou ensemble à partir d'une collection existante
- Permet de remplacer certains traitements qu'on aurait dû faire avec les boucles
- Pour une liste `[f(index) for index in input_seq if condition]` (`input_seq` est une liste, tuple ou toute séquence itérable avec indice)
- Pour une liste `[f(item) for item in input_seq if condition]` (`input_seq` est une liste, tuple ou toute séquence itérable)
- Pour un dictionnaire `{f_key(item):f_value(item) for item in input_seq if condition}` (`input_seq` est une séquence itérable)
- `f, f_key, f_value` sont des fonctions quelconques
- La partie `if condition` est optionnelle
- Il est aussi possible de remplacer les boucles imbriquées par une seule compréhension

```py
--8<--
comprehension.py
--8<--
```

## Utiliser une librairie tierce

- Même si la libraire standard de Python est riche, on a souvent besoin d'utiliser des librairies tierces pour aller plus vite
- Le dépôt standard des librairies Python est [PyPI](https://pypi.org/) (**Py**thon **P**ackage **I**ndex)
- On peut utiliser son moteur de recherche pour trouver un librairie. Par exemple, cherchons la libraire **matplotlib**
- Une fois dans la page de la librairie, on peut trouver la commande qui permet de l'installer localement. Pour **matplotlib**, la commande sera `pip install matplotlib` (si pip n'est pas trouvé alors essayer avec `python -m pip install matplotlib`)
- Ensuite, on pourra utiliser la librairie en se référant à sa documentation. Par exemple, matplotlib propose [des tutoriels](https://matplotlib.org/stable/tutorials/index.html) qui est un bon point de départ.

## Sources et références

- [Python List Comprehension: single, multiple, nested, & more](https://www.learndatasci.com/solutions/python-list-comprehension/)
