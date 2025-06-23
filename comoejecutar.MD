# Documentación para ejecutar el proyecto backend de aguas con django y docker

Seguir paso a paso

3. Levantar entorno de Docker:

   ```
   docker-compose up --build
   ```

4. En caso de error durante el levantamiento:

   Este comando sirve en caso de que ocurra un error durante el levantamiento del entorno para eliminar todo lo que se haya alcanzado a crear

   ```
   docker-compose down
   ```

5. Subir excell del drive llamado 'datos2024(300k).csv' a la raiz del proyecto o crearlo en base al excell original pero con 300k registros solamente (Solo para agilizar tiempos en desarrollo ya que estamos usando sqlite).

6. Ejecutar en una terminal bash

   Esto ejecuta un archivo con todos los comandos necesarios para eliminar de ser necesario los archivos de migraciones, sqlite y el excell limpio para luego cargar los 300k registros a la base de datos sqlite para su uso

   ```
   bash reset.sh
   ```

7. Ir a http://localhost:8000/
