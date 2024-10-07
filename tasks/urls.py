from django.urls import path
from .views import list_tasks, create_task, edit_task, delete_task
urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name = 'create_task'),
    path('/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('/<int:task_id>/delete/', delete_task , name='delete_task')
]