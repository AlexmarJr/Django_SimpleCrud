from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('save', views.createTask, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task")
]