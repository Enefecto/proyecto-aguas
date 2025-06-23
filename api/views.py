from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from .models import Registro
import pyproj

@api_view(['GET'])
def coordenadas_unicas(request):
    registros_vistos = set()
    resultados = []

    transformer = pyproj.Transformer.from_crs("epsg:32719", "epsg:4326", always_xy=True)

    for reg in Registro.objects.all():
        coord = (reg.utm_norte, reg.utm_este)
        if coord not in registros_vistos:
            registros_vistos.add(coord)

            # Agrupar registros por coordenadas
            registros_coord = Registro.objects.filter(
                utm_norte=reg.utm_norte, 
                utm_este=reg.utm_este
            )

            # Promedio de caudal
            avg_caudal = registros_coord.aggregate(avg=Avg('caudal'))['avg']
            avg_caudal = round(avg_caudal, 2) if avg_caudal is not None else None

            # Tomar el primer registro válido para los campos nominales
            primer = registros_coord.first()
            
            nom_cuenca = primer.nom_cuenca if primer.nom_cuenca else "No existe registro"
            nom_sub = primer.nom_subsubcuenca if primer.nom_subsubcuenca else "No existe registro"
            comuna = primer.comuna if primer.comuna else "No existe registro"
            region = primer.region if primer.region else "No existe registro"
            cod_cuenca = primer.cod_cuenca if primer.cod_cuenca else "No existe registro"

            # Transformar coordenadas a lat/lon
            lon, lat = transformer.transform(reg.utm_este, reg.utm_norte)

            resultados.append({
                "lat": lat,
                "lon": lon,
                "utm_norte": reg.utm_norte,
                "utm_este": reg.utm_este,
                "caudal_promedio": avg_caudal,
                "nom_cuenca": nom_cuenca,
                "nom_subsubcuenca": nom_sub,
                "cod_cuenca": cod_cuenca,
                "comuna": comuna,
                "region": region,
                "id": reg.id
            })

    return Response(resultados)
