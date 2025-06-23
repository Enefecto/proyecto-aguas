# Documentación para ejecutar el proyecto

Seguir paso a paso

docker-compose up --build

docker-compose down (Ejecutar este comando en caso de error durante el levantamiento del entorno para eliminar todo lo que se haya alcanzado a crear)

(Se usa el prefijo `docker-compose exec web` para usar el entorno de docker creado)
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

cargar registos (100k)

python api/management/commands/limpiarcsv.py (Limpiar antes)

docker-compose exec web python manage.py cargar_datos
