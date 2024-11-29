from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('task/', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
]
