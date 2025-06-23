from django.urls import path
from .views import coordenadas_unicas

urlpatterns = [
    path('coordenadas/', coordenadas_unicas, name='coordenadas_unicas'),
]
