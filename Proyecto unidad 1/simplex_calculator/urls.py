# simplex_calculator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),  # Página principal
    path('solve_simplex/', views.solve_simplex, name='solve_simplex'),  # Vista que recibe el JSON
    path('resultado/', views.resultado, name='resultado'),  # Nueva ruta para mostrar resultados
]