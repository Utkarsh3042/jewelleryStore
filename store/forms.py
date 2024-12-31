from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomSignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CustomLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

