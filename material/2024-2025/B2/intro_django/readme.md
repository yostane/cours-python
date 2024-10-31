# Django

## Exercices

1. Ajouter une page http://localhost:8000/ynav/hello qui affiche 'Hello World' dans une balise h1
1. Ajouter une page http://localhost:8000/ynav/user/profile qui répond avec un html complet
    - Exemple de contenu:
    ```html
    <html>
    <head>
        <title>Profile</title>
    </head>
    <body>
        <h1>Profile</h1>
        <p>First Name: John</p>
        <p>Last Name: Doe</p>
    </body>
    </html>
    ```
    - Astuce: Utiliser la fonction `HttpResponse` de Django et `"""` pour mettre du texte multi-lignes.
        - Exemple
        ```python
        from django.http import HttpResponse

        def profile(request):
            return HttpResponse("""<html>
            <head>
                <title>Profile</title>
            </head>
            <body>
                <h1>Profile</h1>
                <p>First Name: John</p>
                <p>Last Name: Doe</p>
            </body>
            </html>""")
        ```
