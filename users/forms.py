from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Mot de passe', widget=forms.PasswordInput, help_text=None
    )
    password2 = forms.CharField(
        label='Confirmation mot de passe',
        widget=forms.PasswordInput,
        help_text=None,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nom utilisateur',
        }
        help_texts = {
            'username': None,
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom utilisateur')
    password = forms.CharField(
        label='Mot de passe', widget=forms.PasswordInput
    )
