from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title',]