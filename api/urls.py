from django.urls import path
from .views import coordenadas_unicas, analisis_coordenada

urlpatterns = [
    path('coordenadas/', coordenadas_unicas, name='coordenadas_unicas'),
    path('analisis-coordenada/', analisis_coordenada, name='analisis_coordenada'),
]
