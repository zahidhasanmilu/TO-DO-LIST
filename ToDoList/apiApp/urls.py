from django.urls import path
from  .import views

urlpatterns = [
    path('', views.TaskApi.as_view(), name='taskapi')    
]
