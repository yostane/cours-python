---
title: Exercices de Tkinter
---

# Exercices

!!! warning "Consignes"

    - Ne pas de faire aider par des IA ou genAI
    - Utiliser les composants `ttk` autant que possible

## Série 1

1. Créer une fenêtre qui affiche un bouton dont le texte est un nombre alétoire entre 1 et 100. Chaque fois qu'on clique sur le bouton, le nombre aléatoire change.
1. Créer une fenêtre qui affiche un bouton "Quitter" et un texte editable. Gérer le comportement suivant quand on clique sur le bouton "Quitter":
    - Si on n'a pas modifié le texte, la fenêtre se ferme,
    - Si on a modifié le texte, une boîte de dialogue demande si on veut vraiment quitter. Si on répond "Oui", la fenêtre se ferme, sinon elle reste ouverte (voir astuce plus bas).
1. Créer une fenêtre qui affiche un texte editable et les boutons "sauvegarde" et "charger". Gérer le comportement suivant:
    - Quand on clique sur "sauvegarde", le texte est sauvegardé dans un fichier texte,
    - Quand on clique sur "charger", le texte est chargé depuis le fichier texte et est affiché dans la zone éditable (voir astuce plus bas).

### Astuces

```py title="message box"
import tkinter.messagebox as mb
anwser = mb.askyesno(title="Confirmer?", message="Voulez-vous quitter ?")
```

```py title="Sauvegarder et charger un fichier"
def sauvegarder(texte):
    with open("fichier.txt", "w") as f:
        f.write(texte)

def charger():
    with open("fichier.txt", "r") as f:
        return f.read()
```
