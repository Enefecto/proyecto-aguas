#!/bin/bash

echo "Eliminando archivos..."
rm db.sqlite3
rm datos2024_limpio.csv
rm api/migrations/00*.py

echo "Limpiando CSV dentro del contenedor..."
docker-compose exec web python manage.py limpiarcsv

echo "Creando migraciones..."
docker-compose exec web python manage.py makemigrations

echo "Aplicando migraciones..."
docker-compose exec web python manage.py migrate

echo "Cargando datos..."
docker-compose exec web python manage.py cargar_datos
