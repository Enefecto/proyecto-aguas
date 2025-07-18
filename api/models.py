from django.db import models

class Registro(models.Model):
    id_medicion = models.IntegerField(null=True, blank=True)
    id_informante = models.IntegerField(null=True, blank=True)
    id_junta = models.IntegerField(null=True, blank=True)
    region = models.IntegerField(null=True, blank=True)
    provincia = models.IntegerField(null=True, blank=True)
    comuna = models.IntegerField(null=True, blank=True)
    utm_norte = models.FloatField(null=True, blank=True)
    utm_este = models.FloatField(null=True, blank=True)
    huso = models.IntegerField(null=True, blank=True)
    codigo = models.CharField(max_length=100, null=True, blank=True)
    naturaleza = models.CharField(max_length=100, null=True, blank=True)
    cod_cuenca = models.CharField(max_length=100, null=True, blank=True)
    nom_cuenca = models.CharField(max_length=100, null=True, blank=True)
    cod_acuifero = models.CharField(max_length=100, null=True, blank=True)
    nom_acuifero = models.CharField(max_length=100, null=True, blank=True)
    sector_sha = models.CharField(max_length=100, null=True, blank=True)
    cod_subcuenca = models.CharField(max_length=100, null=True, blank=True)
    nom_subcuenca = models.CharField(max_length=100, null=True, blank=True)
    cod_subsubcuenca = models.CharField(max_length=100, null=True, blank=True)
    nom_subsubcuenca = models.CharField(max_length=100, null=True, blank=True)
    cod_fuente_superficial = models.CharField(max_length=100, null=True, blank=True)
    nom_fuente_superficial = models.CharField(max_length=100, null=True, blank=True)
    nombre_fuente = models.CharField(max_length=100, null=True, blank=True)
    extrae_canal = models.BooleanField(null=True, blank=True)
    nombre_canal = models.CharField(max_length=100, null=True, blank=True)
    apr = models.BooleanField(null=True, blank=True)
    puntoalt = models.CharField(max_length=100, null=True, blank=True)
    tiene_motobomba = models.BooleanField(null=True, blank=True)
    tiene_bocatoma = models.BooleanField(null=True, blank=True)
    tipo_bocatoma = models.CharField(max_length=100, null=True, blank=True)
    descarga_cauce_natural = models.BooleanField(null=True, blank=True)
    habilitada = models.BooleanField(null=True, blank=True)
    motivo_deshabilitada = models.CharField(max_length=100, null=True, blank=True)
    motivo_otra = models.CharField(max_length=100, null=True, blank=True)
    estado_obra = models.IntegerField(null=True, blank=True)
    motivo_cambio_estado = models.CharField(max_length=100, null=True, blank=True)
    fecha_cambio_estado = models.DateTimeField(null=True, blank=True)
    motivo_cambio_informante = models.CharField(max_length=100, null=True, blank=True)
    nombre_obra = models.CharField(max_length=100, null=True, blank=True)
    tipo_obra = models.CharField(max_length=100, null=True, blank=True)
    cod_sector_sha = models.IntegerField(null=True, blank=True)
    representa_junta = models.BooleanField(null=True, blank=True)
    parte_junta = models.BooleanField(null=True, blank=True)
    nombre_usuario_obra = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    id_medicion1 = models.IntegerField(null=True, blank=True)
    id_obra_captacion = models.IntegerField(null=True, blank=True)
    canal_transmision = models.IntegerField(null=True, blank=True)
    tipo_medicion = models.IntegerField(null=True, blank=True)
    fecha_medicion = models.DateTimeField(null=True, blank=True)
    fecha_origen = models.DateTimeField(null=True, blank=True)
    caudal = models.FloatField(null=True, blank=True)
    altura_limnimetrica = models.FloatField(null=True, blank=True)
    totalizador = models.IntegerField(null=True, blank=True)
    nivel_freatico = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Registro {self.id_medicion} - {self.nom_cuenca}"
