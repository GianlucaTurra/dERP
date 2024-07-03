# pylint: disable=missing-class-docstring,missing-module-docstring
from django import forms
from .models import Item


BASIC_STYLE = 'rounded-lg w-full'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': BASIC_STYLE,
            'placeholder': 'New Item'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': BASIC_STYLE,
            'placeholder': 'Brief description'
        })
    )
