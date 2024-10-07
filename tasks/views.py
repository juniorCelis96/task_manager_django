from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
"""summary: This Method permit obtain the tasks list
    params(Type): request(Object): Body of the request
"""
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

"""summary: This Method permit create new tasks
    params(Type): request(Object): Body of the request to storage
"""
def create_task(request):
    print("test: ", request.POST)
    
    # Si el checkbox no está seleccionado, request.POST['completed'] no estará presente.
    completed = request.POST.get('completed', False) == 'on'
    
    task = Task(
        title=request.POST['title'], 
        description=request.POST['description'], 
        completed=completed, 
        quote="Hola mundo xd"
    )
    task.save()
    return redirect('/tasks/')

"""summary: This Method permit Delete the task
    params(Type): request(Object): Body of the request to storage
    params(Type): tasks_id(int): Id row to delete
"""
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/tasks/')

"""summary: This Method permit edit the task
    params(Type): request(Object): Body of the request to storage
    params(Type): tasks_id(int): Id row to edit
"""
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        # Actualizamos los datos del objeto con los datos del formulario
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = request.POST.get('completed', False) == 'on'
        task.quote = 'Editado'
        
        task.save()  # Guardamos los cambios en la base de datos
        return redirect('/tasks/')  # Redirigimos a la lista de tareas

    # Si no es POST, renderizamos el formulario con los datos actuales de la tarea
    return render(request, 'edit_task.html', {'task': task})
