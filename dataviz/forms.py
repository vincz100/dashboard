from django import forms

class HomeForm(forms.Form):
    codgeo = forms.CharField(max_length=5)

class LoginForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)