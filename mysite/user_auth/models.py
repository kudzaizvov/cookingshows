from django.db import models
from django import forms
from django.contrib.auth import authenticate, login

# Create your models here.
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Add your custom validation logic here
        if username and password:
            if not authenticate(username, password):
                raise forms.ValidationError("Invalid login credentials.")

        return super().clean()