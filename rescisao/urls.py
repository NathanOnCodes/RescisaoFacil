from django.urls import path
from .views import calcular_rescisao

urlpatterns = [
    path('api/v1/calcular-rescisao', calcular_rescisao, name='calcular-rescisao'),
]