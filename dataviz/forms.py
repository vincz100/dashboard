from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class TerritoryForm(forms.Form):
    territory = forms.CharField(label="Territoire", max_length=30)

class SearchTerritoryForm(forms.Form):
    scot = forms.CharField()
    epci = forms.CharField()
    commune = forms.CharField()
