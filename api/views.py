from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Sum, Min
from .models import Registro
import pyproj

@api_view(['GET'])
def coordenadas_unicas(request):
    resultados = []

    transformer = pyproj.Transformer.from_crs("epsg:32719", "epsg:4326", always_xy=True)

    # 1. Agrupar por coordenadas y tomar el ID mínimo como referencia
    coordenadas = (
        Registro.objects
        .values("utm_norte", "utm_este")
        .annotate(id=Min("id"))
    )

    # 2. Obtener registros base usando los ID mínimos
    registros_map = Registro.objects.in_bulk([c["id"] for c in coordenadas])

    for coord in coordenadas:
        reg = registros_map[coord["id"]]

        lon, lat = transformer.transform(coord["utm_este"], coord["utm_norte"])

        resultados.append({
            "lat": lat,
            "lon": lon,
            "utm_norte": coord["utm_norte"],
            "utm_este": coord["utm_este"],
            "nom_cuenca": reg.nom_cuenca or "No existe registro",
            "nom_subsubcuenca": reg.nom_subsubcuenca or "No existe registro",
            "cod_cuenca": reg.cod_cuenca or "No existe registro",
            "comuna": reg.comuna or "No existe registro",
            "region": reg.region or "No existe registro",
            "id": reg.id
        })

    return Response(resultados)


@api_view(['POST'])
def analisis_coordenada(request):
    utm_norte = request.data.get("utm_norte")
    utm_este = request.data.get("utm_este")

    if not utm_norte or not utm_este:
        return Response({"error": "utm_norte y utm_este son requeridos"}, status=400)

    registros = Registro.objects.filter(utm_norte=utm_norte, utm_este=utm_este)

    if not registros.exists():
        return Response({"error": "No hay registros para esas coordenadas"}, status=404)

    total_caudal = registros.aggregate(total=Sum("caudal"))["total"] or 0
    promedio_caudal = registros.aggregate(avg=Avg("caudal"))["avg"] or 0

    ranking_informantes = (
        registros.values("id_informante")
        .annotate(total_caudal=Sum("caudal"))
        .order_by("-total_caudal")[:5]
    )

    return Response({
        "total_registros": registros.count(),
        "total_caudal": round(total_caudal, 2),
        "promedio_caudal": round(promedio_caudal, 2),
        "ranking_informantes": list(ranking_informantes)
    })