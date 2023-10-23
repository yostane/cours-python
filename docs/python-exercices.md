# Exercices

!!! warning "Consignes"

    - Ne pas de faire aider par des IA ou genAI

## Série 1

1. Ecrire un script Python qui demande à l’utilisateur de saisir un nombre entier et affiche si ce nombre est pair ou impair. (astuce: utiliser `n = int(input("Saisir un entier : "))`)
1. Ecrire un script Python qui demande à l'utilisateur de saisir un entier n et affiche la somme des n premiers entiers.
1. Ecrire un script Python qui demande à l’utilisateur de saisir un nombre entier et affiche tous les diviseurs de ce nombre.
1. Ecrire un script Python qui génère deux nombres aléatoires x et y avec 0 <= x < 10 et x <= y < 100. (astuce: importer `random` et appeler `x = random.randint(0, 10)`).
1. Ecrire un programme Python qui génère deux nombres aléatoires x et y avec 0 <= x < 10 et x <= y < 100. Le programme affiche ensuite le résultat de la division entière entre y et x et le reste de la division. (penser à gérer le cas où x = 0).
1. Ecrire un programme qui affiche autant de caractères que possible d'une chaîne de caractères  sous forme de suite pyramidale. (astuce: on peut faire un for in sur une chaîne de caractères `for char in chaine`).
    - Exemple pour la chaîne "abcdefghijklmnopqrstuvwxyz" * 10

    ```
    a 
    bc 
    def 
    ghij 
    klmno 
    pqrstu 
    vwxyzab 
    cdefghij 
    klmnopqrs 
    tuvwxyzabc 
    defghijklmn 
    opqrstuvwxyz 
    abcdefghijklm 
    nopqrstuvwxyza 
    bcdefghijklmnop 
    qrstuvwxyzabcdef 
    ghijklmnopqrstuvw 
    xyzabcdefghijklmno 
    pqrstuvwxyzabcdefgh 
    ijklmnopqrstuvwxyzab 
    cdefghijklmnopqrstuvw 
    xyzabcdefghijklmnopqrs
    ```

    - Réponse incorrecte pour la "abcdefghijklmnopqrstuvwxyz"

    ```
    Incorrect
    a 
    bc 
    def 
    ghij 
    klmno 
    pqrstu 
    vwxyz

    Correct
    a 
    bc 
    def 
    ghij 
    klmno 
    pqrstu 
    ```

1. Écrire une fonction `count_letters(texte)` ayant pour argument une chaîne de caractères texte et qui renvoie un dictionnaire qui contient la fréquence de toutes les lettres de la chaîne entrée. Par exemple: `count_letters("hello")` renvoie `{"h": 1, "e": 1, "l": 2, "o": 1}`.
1. Soit des rectangles définis avec des dictionnaires dont les clés sont `"x", "y", "largeur", "hauteur"`.
    - Ecrire une fonction `is_intersecting(rectangle1, rectangle2)` qui retourne `True` s'il y a intersection entre les deux rectangles.
    - Ecrire une fonction `get_intersection(rectangle1, rectangle2)` qui retourne le rectangle intersection s'il existe, sinon `None`.
1. Ecrire une fonction `fx_square(x)` qui retourne le résultat de `x * x`.
    - Ecrire une fonction `fx_square_list(n)` qui retourne une liste de n éléments. La valeur d'un élément d'indice `i` est `fx_square(i)`.
    - Utiliser la librairie `matplotlib` pour dessiner un graphique dont les abscisses sont les entiers allant de 0 à n et les ordonnées sont les éléments retournés par `fx_square_list(n)`.
1. Définir une fonction `fx_square_list2(points)` qui prend en argument une liste d'entiers ordonnées par ordre croissant et retourne une nouvelle liste dont la valeur du i ème élément est `points[i] * points[i]`.
    - Tracer le graphique de **f(x) = x * x** pour x compris entre -100 à 100.
1. Faire le graphique de -100 à 100 des fonctions suivantes: `exp(x)`, `1/x`, `log(x) + (1/(x puissance3))`

## Corrigés série 1

??? "Exos pyramide, count_letters et intersection"

    ```py
    --8<--
    exercices_part1.py
    --8<--
    ```

??? "plot"

    ```py
    --8<--
    exercices_part1_plot.py
    --8<--
    ```

## Série 2

Résoudre les exercices suivants avec les compréhensions.

1. Créer une liste des 10 premiers nombres pairs
1. Créer un dictionnaire contentant 10 clé allant de 0 à 9. La valeur de chaque clé est une texte indiquant la parité du nombre. (exemple: {0: "paire", 1: "impaire", etc.})
1. Créer un dictionnaire contentant 10 clé allant de 0 à 9 convertie en string. La valeur de chaque clé est une texte indiquant la parité du nombre. (exemple: {"0": "paire", "1": "impaire", etc.})
1. Créer un dictionnaire qui filtre le dictionnaire précédent en ne gardant que les nombres impairs

## Source

- [Exercices corrigés d'algorithmique Python - Les bases](https://www.tresfacile.net/tp-python-exercices-corriges-dalgorithmique-python-les-bases/)
- [Exercices du site développez](https://algo.developpez.com/exercices/)
- [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)
- [Sites pour apprendre en s’amusant](https://info.blaisepascal.fr/exercices-python/)
