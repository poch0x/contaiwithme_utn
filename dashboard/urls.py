from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('perfil/', views.perfil, name="perfil"),
    path('configuracion/', views.configuracion, name="configuracion"),
    path('servicios/', views.servicios, name="servicios"),
    path('listar-servicios/', views.listar_servicios, name="listar_servicios"),
    path('obtener_servicio/<int:servicio_id>/', views.obtener_servicio, name='obtener_servicio'),
    path('editar_servicio/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar-servicio/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('crear-servicio/', views.crear_servicio, name='crear_servicio'),
]
