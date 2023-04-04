from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Task Create Successfully")
            return redirect('home')

    context={
        'task': tasks,
        'form': form,
    }
    return render(request, 'index.html', context)




def update(request,id):
    task = Task.objects.get(id=id)
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Task Has Been Updated")
            return redirect('home')
        else:
            messages.error(request, "Please INPUT DATA")
            return redirect('update')
    else:
        form = TaskForm(instance=task)
    context={
        'form': form,
        'task': task,
    }
    return render(request, 'update.html', context)

def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        messages.success(request, "Your Task Has Been Delete!")
        return redirect('home')
    context={
        'task': task,
    }
    return render(request, 'delete.html', context)

def forcedelete(request):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, "Your Task Has Been Delete!")
    return redirect('home')