from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",max_length=20,widget=forms.TextInput())

    password1 = forms.CharField(label='',widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')