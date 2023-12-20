from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from taskApp.models import Task
from apiApp.serializers import TaskSerializers

# Create your views here.
class TaskApi(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers