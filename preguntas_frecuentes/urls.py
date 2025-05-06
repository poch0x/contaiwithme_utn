from django.urls import path
from . import views  # Asegúrate de importar la vista correcta

urlpatterns = [
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
]