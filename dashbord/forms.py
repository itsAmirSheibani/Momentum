from django import forms
from .models import *


"""class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title', 'description', 'category', 'priority',
            'dute_date', 'due_time', 

        ]
"""
class ReflectionForm(forms.ModelForm):

    class Meta:
        model = Reflection

        fields = ['content']