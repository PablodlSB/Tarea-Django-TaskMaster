## ▶️ Instrucciones para ejecutar el proyecto en local

### 1. Descargar el proyecto

Descomprimir el archivo `.zip` y abrir una terminal en la carpeta raíz del proyecto.

### 2. Crear un entorno virtual

python -m venv venv

### 3. Activar el entorno virtual

**Windows (PowerShell):**

.\venv\Scripts\Activate

Cuando el entorno esté activo aparecerá `(venv)` al inicio de la línea de comandos.

### 4. Instalar dependencias

Si existe el archivo `requirements.txt`:

pip install -r requirements.txt

Si no existe:

pip install django faker mysqlclient whitenoise

### 5. Aplicar migraciones de la base de datos

python manage.py makemigrations
python manage.py migrate

Esto creará todas las tablas necesarias en la base de datos.

### 6. Crear un superusuario (acceso al admin)

python manage.py createsuperuser

Introduce usuario, email y contraseña cuando se solicite.

### 7. Poblar la base de datos con datos de prueba (opcional)

python populate_tasks.py

Este script crea usuarios, proyectos y tareas de ejemplo.

### 8. Ejecutar el servidor de desarrollo

python manage.py runserver

Acceder a la aplicación desde el navegador:

* Aplicación: [http://127.0.0.1:8000/]
* Panel de administración: [http://127.0.0.1:8000/admin]

### 9. Nota importante

Cada vez que se abra el proyecto en una nueva terminal, es necesario **activar el entorno virtual** antes de ejecutar cualquier comando.
