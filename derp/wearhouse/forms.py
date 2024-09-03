# pylint: disable=missing-class-docstring,missing-module-docstring
from django import forms

from .models import Wearhouse


BASIC_STYLE = 'rounded-lg w-full'


class WearhouseForm(forms.ModelForm):
    class Meta:
        model = Wearhouse
        fields = ['name', 'description', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': BASIC_STYLE,
                'placeholder': 'Some name'
            }),
            'description': forms.Textarea(attrs={
                'class': BASIC_STYLE,
                'placeholder': 'Some brief description'
            }),
            'address': forms.TextInput(attrs={
                'class': BASIC_STYLE,
                'placeholder': 'Wearhouse address'
            })
        }
