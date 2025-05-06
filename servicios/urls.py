from django.urls import path
from servicios import views
from .views import get_costo_base
from .views import get_servicios
from .views import obtener_servicios_json

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.get_servicios, name="get_servicios"),  # Nueva ruta para obtener todos los servicios
    path('admin/servicios/servicio/<int:servicio_id>/cahnge/get_costo_base/', get_costo_base, name='get_costo_base'),
    path('obtener_servicios/', obtener_servicios_json, name='obtener_servicios'),


]
