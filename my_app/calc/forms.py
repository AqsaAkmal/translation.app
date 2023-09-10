# forms.py
from django import forms

class ButtonForm(forms.Form):
    submit = forms.CharField(widget=forms.HiddenInput, required=False)
    listen = forms.CharField(widget=forms.HiddenInput, required=False)
