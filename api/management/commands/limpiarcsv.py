import csv
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Limpia el archivo datos2024(100k).csv y genera datos2024_limpio.csv'

    def handle(self, *args, **kwargs):
        input_file = 'datos2024(300k).csv'
        output_file = 'datos2024_limpio.csv'

        if not os.path.exists(input_file):
            self.stderr.write(self.style.ERROR(f"El archivo {input_file} no existe."))
            return

        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                # Si hay una sola celda, dividimos la fila por comas manualmente
                if len(row) == 1:
                    row = row[0].strip('"').split(',')  # Quita comillas externas y separa por coma
                writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f"Archivo limpiado correctamente. Guardado en {output_file}"))
