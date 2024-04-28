from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Insira o seu usuário",
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
     
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Insira a sua senha",
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
