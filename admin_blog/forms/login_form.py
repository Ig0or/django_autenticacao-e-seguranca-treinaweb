from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import fields
from ..models import Usuario
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ['username', 'password']