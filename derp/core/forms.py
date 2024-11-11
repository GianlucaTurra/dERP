from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms


INPUT_CLASSES: str = "border block w-full"


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": _("Your user name"), "class": INPUT_CLASSES}
        ),
        label=_("Username"),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": _("Your password"), "class": INPUT_CLASSES}
        ),
        label=_("Password"),
        required=True,
    )
