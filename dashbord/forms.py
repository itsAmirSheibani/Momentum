from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Task, Reflection, Transaction, Goal

"""
the widgets in each class, is customized to match the Momentum UI.
"""


# Form used to create and edit tasks.
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title', 'description', 'category', 'priority',
            'due_time',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'momentum-form__input',
                'placeholder': 'e.g. Finish Django models',
            }),
            'description': forms.Textarea(attrs={
                'class': 'momentum-form__textarea',
                'rows': 4,
                'placeholder': 'Optional short description...',
            }),
            'category': forms.TextInput(attrs={
                'class': 'momentum-form__input',
                'placeholder': 'e.g. Backend, University',
            }),
            'priority': forms.Select(attrs={
                'class': 'momentum-form__select',
            }),
            'due_time': forms.TimeInput(attrs={
                'class': 'momentum-form__input',
                'type': 'time',
            }),
        }


# Form used to create and edit journals.
class ReflectionForm(forms.ModelForm):

    class Meta:
        model = Reflection

        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'momentum-form__textarea',
                'rows': 5,
                'placeholder': "What happened today?",
            }),
        }


# Form used to create and edit transactions.
class FinanceForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = ['type', 'description', 'date', 'amount']

        widgets = {
            'type': forms.Select(attrs={
                'class': 'momentum-form__select',
            }),
            'description': forms.TextInput(attrs={
                'class': 'momentum-form__input',
                'placeholder': 'e.g. Groceries, Freelance payment',
            }),
            'date': forms.DateInput(attrs={
                'class': 'momentum-form__input',
                'type': 'date',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'momentum-form__input',
                'step': '0.01',
                'placeholder': '0.00',
            }),
        }


# Form used to create and edit goals.
class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal

        fields = ['title', 'target_date', 'progress']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'momentum-form__input',
                'placeholder': 'e.g. Learn German (A2)',
            }),
            'target_date': forms.DateInput(attrs={
                'class': 'momentum-form__input',
                'type': 'date',
            }),
            'progress': forms.NumberInput(attrs={
                'class': 'momentum-form__input',
                'min': 0,
                'max': 100,
                'placeholder': '0–100',
            }),
        }


# Form used to update the user's profile information.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'momentum-input'}),
            'last_name': forms.TextInput(attrs={'class': 'momentum-input'}),
            'email': forms.EmailInput(attrs={'class': 'momentum-input'}),
        }


# Customizes Django's password change form to use.
class MomentumPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'momentum-input'})
