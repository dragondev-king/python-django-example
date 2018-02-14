"""Simple Page Forms"""
from django import forms

nameform_widget = forms.TextInput(attrs={
    'class': 'form-control',
    'max_length': '100',
    'placeholder': 'Your GitHub Name',
    'autofocus': 'true'
})
class NameForm(forms.Form):
    """Name Form"""
    name = forms.CharField(required=True, widget=nameform_widget)
