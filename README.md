README: API REST para Gestión de Tareas con Citas Motivacionales
Descripción
Esta aplicación Django proporciona una API RESTful para gestionar tareas, incluyendo la creación, listado y eliminación de las mismas. Además, consume una API externa de citas motivacionales para asociar una cita inspiradora a cada tarea creada. La interfaz de usuario ofrece una vista sencilla de las tareas, con formularios para su creación y edición.

Funcionalidades
API REST:
Creación de tareas: POST /api/tasks
Listado de tareas: GET /api/tasks
Eliminación de tareas: DELETE /api/tasks/{id}
Integración de API externa:
Consumo de una API pública de citas motivacionales (ejemplo: Quotes REST API).
Asociación de una cita motivacional a cada nueva tarea.
Interfaz de usuario:
Página principal con listado de tareas.
Formularios para crear y editar tareas.
Botones para eliminar tareas.
Visualización de la cita motivacional asociada a cada tarea.
Instalación y ejecución

1. Clonar el repositorio:
Bash
git clone https://github.com/juniorCelis96/task_manager_django.git

2. Crear un entorno virtual:
Bash
python -m venv venv
source venv/bin/activate
Usa el código con precaución.

3. Instalar las dependencias:
Bash
pip install -r requirements.txt
Usa el código con precaución.

4. Configurar la base de datos:
Editar el archivo settings.py con los detalles de tu base de datos.
Realizar las migraciones:
Bash
python manage.py migrate
Usa el código con precaución.

5. Iniciar el servidor de desarrollo:
Bash
python manage.py runserver
Usa el código con precaución.

6. Estructura del proyecto
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    tasks/
        __init__.py
        models.py
        serializers.py
        views.py
