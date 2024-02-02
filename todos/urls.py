from django.urls import path
from .views import task_list, add_task, delete_task, edit_task, toggle_completed

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
     path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('toggle/<int:task_id>/', toggle_completed, name='toggle_completed'),

]
