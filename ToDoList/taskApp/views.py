from django.shortcuts import render
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all()




    context={
        'tasks': tasks,

    }
    return render(request, 'index.html', context)


def update(request,id):
    task = Task.objects.get(id=id)
    print(task)
    return render(request, 'update.html')

def delete(request,id):
    task = Task.objects.get(id=id)
    print(task)
    return render(request, 'update.html')