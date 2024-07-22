# pylint: disable=missing-class-docstring,missing-module-docstring
from django import forms
from .models import Item


BASIC_STYLE = 'rounded-lg w-full'
DIMENSIONS_STYLE = 'rounded-lg w-full'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'volume_cm3', 'weigth_g']

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
    volume_cm3 = forms.FloatField(
        label='Volume in cm3',
        widget=forms.NumberInput({
            'class': DIMENSIONS_STYLE,
            'placeholder': 0.00,
            'step': 0.01
        }))
    weigth_g = forms.FloatField(
        label='Weigth in grams',
        widget=forms.NumberInput({
            'class': DIMENSIONS_STYLE,
            'placeholder': 0.00,
            'step': 0.01
        }))
