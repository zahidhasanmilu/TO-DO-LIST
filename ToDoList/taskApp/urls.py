from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-task/<str:id>/', views.update, name='updateTask'),
    path('delete-task/<str:id>/', views.delete, name='deleteTask'),
    path('force-delete/<str:id>/', views.forcedelete, name='forcedelete'),
]
