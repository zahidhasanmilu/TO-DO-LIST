from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'You can discribe your task here'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title here'}),
        }