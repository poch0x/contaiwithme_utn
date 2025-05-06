from django.contrib import admin
from django import forms
from contratos.models import Contrato
from clientes.models import Cliente
from django.utils.safestring import mark_safe
from django.shortcuts import render


from contratos.models import LogActividad


class LogActividadInline(admin.TabularInline):
    model = LogActividad
    extra = 0  # No mostrar formularios adicionales vacíos por defecto
    fields = ['mensaje', 'fecha_registro']
    readonly_fields = ['fecha_registro']
    ordering = ['-fecha_registro']  # Ordenar por fecha de registro descendente

admin.site.register(LogActividad)


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['cliente', 'servicio', 'fecha_inicio', 'fecha_fin', 'costo_total']
    
    # Sobrescribir el campo 'costo_total' para que se actualice automáticamente en el admin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Agregar el JS al formulario
        self.fields['costo_total'].widget.attrs['readonly'] = 'readonly'


class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0  # No mostrar formularios adicionales vacíos por defecto
    fields = ['servicio', 'fecha_inicio', 'fecha_fin', 'costo_total']
    readonly_fields = ['costo_total']


# Verificar y desregistrar Cliente si ya está registrado
if admin.site.is_registered(Cliente):
    admin.site.unregister(Cliente)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [ContratoInline]  # Mostrar los contratos relacionados con el Cliente
    list_display = ['nombre_empresa', 'direccion', 'fecha_registro']


# Configuración para el modelo Contrato
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    form = ContratoForm  # Usar el formulario personalizado
    list_display = ['cliente', 'servicio', 'fecha_inicio', 'fecha_fin', 'costo_total', 'estado_coloreado']
    list_filter = ['fecha_inicio', 'fecha_fin', 'servicio']
    search_fields = ['cliente__nombre_empresa', 'servicio__nombre']  # Permite buscar por cliente o servicio
    ordering = ['fecha_inicio']
    actions = ['generar_contrato']    
    
    
    # def generar_contrato(self, request, queryset):
    #     """Método para generar un contrato."""
    #     response = HttpResponse(content_type='application/json')
    #     serializers.serialize('json', queryset, stream=response)
    #     return response
        
    def generar_contrato(self, request, queryset):
        contratos = queryset  # Usamos el queryset recibido
        total = sum(contrato.costo_total for contrato in contratos)  # Sumar los costos totales de los contratos seleccionados
        params = {
            'contratos': contratos,
            'total': total
        }
        return render(request, 'contratos/facturas/factura.html', params)

        
    def estado_coloreado(self, obj):
        """Muestra el estado con un fondo de color y bordes redondeados en Django Admin."""
        colores = {
            'vigente': '#28a745',  # Verde
            'pronto_a_vencer': '#ffc107',  # Amarillo
            'vencido': '#dc3545',  # Rojo
        }
        color = colores.get(obj.estado, '#6c757d')  # Gris por defecto si no coincide
        return mark_safe(
            f'<span style="background-color: {color}; color: white; padding: 5px 10px; '
            f'border-radius: 10px; font-weight: bold;">{obj.get_estado_display()}</span>'
        )

    estado_coloreado.admin_order_field = 'estado'
    estado_coloreado.short_description = 'Estado'

    # Método para guardar el costo_total automáticamente al guardar el contrato
    def save_model(self, request, obj, form, change):
        if obj.servicio:  # Verificar si se ha seleccionado un servicio
            servicio = obj.servicio
            obj.costo_total = servicio.costo_base  # Asignar el costo_base del servicio al campo costo_total
        super().save_model(request, obj, form, change)

    # Inyectar JavaScript en el formulario de administración
    class Media:
        js = ('admin/js/costo_total.js',)
        
        

