from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = [
            'title',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Task name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
