# pylint: disable=missing-class-docstring,missing-module-docstring
from django import forms
from .models import Item
from .modules.measure_units import VOLUME, WEIGTH


BASIC_STYLE = 'rounded-lg w-full'
DIMENSIONS_STYLE = 'rounded-lg w-full'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'volume', 'weigth', 'volume_measure', 'weigth_measure']
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': BASIC_STYLE,
                    'placeholder': 'Some name'
                }),
                'description': forms.Textarea(attrs={
                    'class': BASIC_STYLE,
                    'placeholder': 'Some brief description'
                }),
                'volume': forms.NumberInput(attrs={
                    'class': DIMENSIONS_STYLE
                }),
                'weigth': forms.NumberInput(attrs={
                    'class': f'{DIMENSIONS_STYLE}'
                }),
                'volume_measure': forms.Select(attrs={
                    'class': BASIC_STYLE
                }),
                'weigth_measure': forms.Select(attrs={
                    'class': f'{BASIC_STYLE}'
                }),
            }
