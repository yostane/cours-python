from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PromptForm(forms.Form):
    # doit être pareil quel l'attribut name de l'input
    query = forms.CharField(label="query", max_length=100)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
