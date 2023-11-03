from django import forms


class PromptForm(forms.Form):
    # doit être pareil quel l'attribut name de l'input
    query = forms.CharField(label="query", max_length=100)
