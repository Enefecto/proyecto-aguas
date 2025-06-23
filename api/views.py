import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registro
from .serializers import RegistroSerializer

@api_view(['GET'])
def registros_aleatorios(request):
    registros = list(Registro.objects.all())
    muestra = random.sample(registros, min(len(registros), 10))
    serializer = RegistroSerializer(muestra, many=True)
    return Response(serializer.data)
