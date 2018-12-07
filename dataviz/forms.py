from django import forms

class HomeForm(forms.Form):
    codgeo = forms.CharField(max_length=5)