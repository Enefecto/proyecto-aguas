from django.urls import path
from .views import registros_aleatorios

urlpatterns = [
    path('registros-aleatorios/', registros_aleatorios, name='registros_aleatorios'),
]
