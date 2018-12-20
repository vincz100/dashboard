from django import forms

class TerritoryForm(forms.Form):
    territory = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

