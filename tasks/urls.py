from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksManager.list_tasks),
    path('new/', TasksManager.create_task, name = 'create_task'),
    path('<int:task_id>/edit', TasksManager.edit_task, name='edit_task'),
    path('<int:task_id>/delete', TasksManager.delete_task , name='delete_task')
]