from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """
    Custom registration form for creating a new user account.
    """
    
    username = forms.CharField(
        label="", max_length=20, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
