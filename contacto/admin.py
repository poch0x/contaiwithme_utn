from django.contrib import admin

from .models import Consulta
from .models import Respuesta


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0


class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ['estado_de_respuesta', 'nombre', 'descripcion', 'mail', 'celular', 'fecha']
    list_filter = ['estado_respuesta', 'fecha']
    search_fields = ['nombre', 'descripcion', 'estado_respuesta']


admin.site.register(Consulta, ConsultaAdmin)

