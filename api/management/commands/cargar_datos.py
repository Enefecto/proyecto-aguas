import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Registro

class Command(BaseCommand):
    help = 'Carga datos desde datos2024_limpio.csv en la base de datos'

    def handle(self, *args, **kwargs):
        with open('datos2024_limpio.csv', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')


            
            registros = []
            for row in reader:
                try:
                    registros.append(Registro(
                        id_medicion=self.to_int(row['ID_MEDICION']),
                        id_informante=self.to_int(row['ID_INFORMANTE']),
                        id_junta=self.to_int(row['ID_JUNTA']),
                        region=self.to_int(row['REGION']),
                        provincia=self.to_int(row['PROVINCIA']),
                        comuna=self.to_int(row['COMUNA']),
                        utm_norte=self.to_float(row['UTM_NORTE']),
                        utm_este=self.to_float(row['UTM_ESTE']),
                        huso=self.to_int(row['HUSO']),
                        codigo=row['CODIGO'],
                        naturaleza=row['NATURALEZA'],
                        cod_cuenca=row['COD_CUENCA'],
                        nom_cuenca=row['NOM_CUENCA'],
                        cod_acuifero=row['COD_ACUIFERO'],
                        nom_acuifero=row['NOM_ACUIFERO'],
                        sector_sha=row['SECTOR_SHA'],
                        cod_subcuenca=row['COD_SUBCUENCA'],
                        nom_subcuenca=row['NOM_SUBCUENCA'],
                        cod_subsubcuenca=row['COD_SUBSUBCUENCA'],
                        nom_subsubcuenca=row['NOM_SUBSUBCUENCA'],
                        cod_fuente_superficial=row['COD_FUENTE_SUPERFICIAL'],
                        nom_fuente_superficial=row['NOM_FUENTE_SUPERFICIAL'],
                        nombre_fuente=row['NOMBRE_FUENTE'],
                        extrae_canal=self.to_bool(row['EXTRAE_CANAL']),
                        nombre_canal=row['NOMBRE_CANAL'],
                        apr=self.to_bool(row['APR']),
                        puntoalt=row['PUNTOALT'],
                        tiene_motobomba=self.to_bool(row['TIENE_MOTOBOMBA']),
                        tiene_bocatoma=self.to_bool(row['TIENE_BOCATOMA']),
                        tipo_bocatoma=row['TIPO_BOCATOMA'],
                        descarga_cauce_natural=self.to_bool(row['DESCARGA_CAUCE_NATURAL']),
                        habilitada=self.to_bool(row['HABILITADA']),
                        motivo_deshabilitada=row['MOTIVO_DESHABILITADA'],
                        motivo_otra=row['MOTIVO_OTRA'],
                        estado_obra=self.to_int(row['ESTADO_OBRA']),
                        motivo_cambio_estado=row['MOTIVO_CAMBIO_ESTADO'],
                        fecha_cambio_estado=self.to_date(row['FECHA_CAMBIO_ESTADO']),
                        motivo_cambio_informante=row['MOTIVO_CAMBIO_INFORMANTE'],
                        nombre_obra=row['NOMBRE_OBRA'],
                        tipo_obra=row['TIPO_OBRA'],
                        cod_sector_sha=self.to_int(row['COD_SECTOR_SHA']),
                        representa_junta=self.to_bool(row['REPRESENTA_JUNTA']),
                        parte_junta=self.to_bool(row['PARTE_JUNTA']),
                        nombre_usuario_obra=row['NOMBRE USUARIO OBRA'],
                        apellido_paterno=row['APELLIDO PATERNO'],
                        apellido_materno=row['APELLIDO MATERNO'],
                        id_medicion1=self.to_int(row['ID_MEDICION1']),
                        id_obra_captacion=self.to_int(row['ID_OBRA_CAPTACION']),
                        canal_transmision=self.to_int(row['CANAL_TRANSMISION']),
                        tipo_medicion=self.to_int(row['TIPO_MEDICION']),
                        fecha_medicion=self.to_date(row['FECHA_MEDICION']),
                        fecha_origen=self.to_date(row['FECHA_ORIGEN']),
                        caudal=self.to_float(row['CAUDAL']),
                        altura_limnimetrica=self.to_float(row['ALTURA_LIMNIMETRICA']),
                        totalizador=self.to_int(row['TOTALIZADOR']),
                        nivel_freatico=self.to_float(row['NIVEL_FREATICO']),
                    ))
                except Exception as e:
                    self.stderr.write(f"Error en fila: {row}\n{e}")
            Registro.objects.bulk_create(registros)
            self.stdout.write(self.style.SUCCESS(f'Se cargaron {len(registros)} registros exitosamente.'))

    def to_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError, AttributeError):
            return None


    def to_float(self, value):
        return float(value) if value.strip() else None

    def to_bool(self, value):
        return value.strip().lower() == 'true'

    def to_date(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S') if value.strip() else None
        except ValueError:
            return None
