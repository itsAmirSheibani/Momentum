from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms
from .forms import SignUpForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('/')
        else:
            return redirect('accounts:signup')
    else:

        print("FORM ERRORS:", form.errors)
        return render(request, 'accounts/signup.html', {'form': form})
