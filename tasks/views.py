import http.client
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task

CAPITALES_COORDENADAS = {
    'Bogotá': {'lat': 4.60971, 'lon': -74.08175},
    'Medellín': {'lat': 6.2442, 'lon': -75.5812},
    'Cali': {'lat': 3.43722, 'lon': -76.5225},
    'Barranquilla': {'lat': 10.96854, 'lon': -74.78132},
    'Cartagena': {'lat': 10.39972, 'lon': -75.51444},
    # Agrega el resto de las capitales aquí
}

API_KEY = '775eb8a6e88549c3113d85370350d1b9'
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
    title = request.POST.get('title')
    description = request.POST.get('description')
    completed = request.POST.get('completed') == 'on'
    quote = generar_quote(request)
    # Aquí puedes guardar la tarea y también usar los datos del clima si lo deseas
    task = Task(title=title, description=description, completed=completed, quote=quote)
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
        task.quote = generar_quote(request=request)
        
        task.save()  # Guardamos los cambios en la base de datos
        return redirect('/tasks/')  # Redirigimos a la lista de tareas

    # Si no es POST, renderizamos el formulario con los datos actuales de la tarea
    return render(request, 'edit_task.html', {'task': task})

def generar_quote(request):
    api_key = API_KEY
    lat = None
    lon = None
    if request.method == 'POST':
        capital = request.POST.get('capital')

        # Obtener las coordenadas de la capital seleccionada
        coordinates = CAPITALES_COORDENADAS.get(capital)

        if coordinates:
            lat = coordinates['lat']
            lon = coordinates['lon']

            conn = http.client.HTTPSConnection("api.openweathermap.org")

            url = f"/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

            conn.request("GET", url)

            response = conn.getresponse()
            data = response.read()
            weather_data = json.loads(data)

            # Convertir la temperatura de Kelvin a Celsius
            temp_celsius = weather_data['main']['temp'] - 273.15
            feels_like_celsius = weather_data['main']['feels_like'] - 273.15

            # Generar la variable quote con la información relevante
            quote = f"El clima en {weather_data['name']} es {weather_data['weather'][0]['description']}. " \
                    f"La temperatura actual es de {temp_celsius:.2f}°C, con una sensación térmica de {feels_like_celsius:.2f}°C. " \
                    f"La humedad es del {weather_data['main']['humidity']}% y la velocidad del viento es de {weather_data['wind']['speed']} m/s."

            conn.close()
    return quote