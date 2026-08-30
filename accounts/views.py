from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


def login_view(request):
    """
    Authenticate the user and log them into the application.
    """
    
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
    """
    Log the current user out and show the logout confirmation page.
    """

    logout(request)
    return render(request, 'accounts/logout.html')


def signup_view(request):
    """
    Create a new user account and log the user in after registration.
    """

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect("/")

    return render(request, "accounts/signup.html", {"form": form})
