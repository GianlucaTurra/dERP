# pylint: disable=missing-class-docstring,missing-module-docstring
from django import forms
from .models import Item


BASIC_STYLE = 'rounded-lg w-full'
DIMENSIONS_STYLE = 'rounded-lg w-full'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'height_mm', 'width_mm', 'depth_mm', 'weigth_g']

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
    height_mm = forms.FloatField(
        label='Height in millimeters',
        widget=forms.NumberInput({
            'class': DIMENSIONS_STYLE,
            'placeholder': 0.00,
            'step': 0.01
        }))
    width_mm = forms.FloatField(
        label='Width in millimeters',
        widget=forms.NumberInput({
            'class': DIMENSIONS_STYLE,
            'placeholder': 0.00,
            'step': 0.01
        }))
    depth_mm = forms.FloatField(
        label='Depth in millimeters',
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
