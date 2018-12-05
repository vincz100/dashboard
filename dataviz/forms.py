from django import forms

class InitForm(forms.Form):
    codgeo = forms.CharField(max_length=5)

