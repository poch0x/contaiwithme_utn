from django.contrib import admin
from django.db import connection
from django.utils.safestring import mark_safe
from .models import Servicio

class ServicioInline(admin.TabularInline):
    model = Servicio
    extra = 0

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Datos Generales",
            {
                "fields": [
                    'nombre', 'descripcion', 'costo_base', 'categoria', 'imagen', 'estado', 'ventajas'
                ]
            }
        )
    ]
    
    list_display = ['nombre', 'descripcion', 'costo_base', 'categoria', 'imagen_html', 'estado_coloreado', 'ventajas']
    ordering = ['costo_base']
    list_filter = ['nombre', 'categoria']
    search_fields = ['nombre', 'costo_base', 'categoria']
    actions = ['activar_servicios', 'desactivar_servicios', 'poblar_servicios']
    
    def estado_coloreado(self, obj):
        """Muestra el estado con un fondo de color y bordes redondeados en Django Admin."""
        colores = {
            'Activo': '#28a745',  # Verde
            'Inactivo': '#dc3545',  # Rojo
        }
        color = colores.get(obj.estado, '#6c757d')  # Gris por defecto si no coincide
        return mark_safe(
            f'<span style="background-color: {color}; color: white; padding: 5px 10px; '
            f'border-radius: 10px; font-weight: bold;">{obj.get_estado_display()}</span>'
        )

    estado_coloreado.admin_order_field = 'estado'
    estado_coloreado.short_description = 'Estado'
    
    def activar_servicios(self, request, queryset):
        """Activa los servicios seleccionados."""
        registro = queryset.update(estado='Activo')
        self.message_user(request, f'Se han activado {registro} servicios.')
        
    def desactivar_servicios(self, request, queryset):
        """Desactiva los servicios seleccionados."""
        registro2 = queryset.update(estado='Inactivo')
        self.message_user(request, f'Se han desactivado {registro2} servicios.')

    def poblar_servicios(self, request, queryset):
        """Puebla la base de datos con servicios predeterminados."""

        # Definir los servicios predeterminados
        # servicios = [
        #     ('Automatización de Procesos', 'Automatización de tareas repetitivas para empresas.', '2024-03-05 10:00:00', 500.00, 'Automatizacion', 'images/servicios/servicio1.png', 'Activo'),
        #     ('Chatbot para Atención', 'Desarrollo de chatbot con IA para atención al cliente.', '2024-03-05 10:10:00', 700.00, 'Chatbots', 'images/servicios/servicio2.png', 'Activo'),
        #     ('Limpieza de Datos Empresariales', 'Optimización y limpieza de datos para análisis.', '2024-03-05 10:20:00', 300.00, 'Limpieza de Datos', 'images/servicios/servicio3.png', 'Inactivo'),
        #     ('Automatización en Finanzas', 'Automatización de reportes financieros.', '2024-03-05 10:30:00', 450.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo'),
        #     ('Chatbot para Reservas', 'Sistema automatizado de reservas con chatbot.', '2024-03-05 10:40:00', 650.00, 'Chatbots', 'images/servicios/servicio3.png', 'Inactivo'),
        #     ('Normalización de Datos', 'Corrección y estructuración de bases de datos.', '2024-03-05 10:50:00', 250.00, 'Limpieza de Datos', 'images/servicios/servicio1.png', 'Activo'),
        #     ('Automatización de Facturación', 'Automatización de emisión de facturas y recibos.', '2024-03-05 11:00:00', 550.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo'),
        #     ('Chatbot para Soporte Técnico', 'Asistente virtual para resolución de incidencias.', '2024-03-05 11:10:00', 800.00, 'Chatbots', 'images/servicios/servicio2.png', 'Inactivo'),
        #     ('Depuración de Datos Duplicados', 'Eliminación de registros duplicados en bases de datos.', '2024-03-05 11:20:00', 280.00, 'Limpieza de Datos', 'images/servicios/servicio1.png', 'Activo'),
        #     ('Automatización de Marketing', 'Automatización de campañas de email y redes sociales.', '2024-03-05 11:30:00', 600.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo')
        # ]
        servicios = [
            ('Automatización de Procesos', 'Automatización de tareas repetitivas para empresas.', '2024-03-05 10:00:00', 500.00, 'Automatizacion', 'images/servicios/servicio1.png', 'Activo', 'Ahorra tiempo y reduce errores en tareas repetitivas.'),
            ('Chatbot para Atención', 'Desarrollo de chatbot con IA para atención al cliente.', '2024-03-05 10:10:00', 700.00, 'Chatbots', 'images/servicios/servicio2.png', 'Activo', 'Mejora la experiencia del cliente con respuestas rápidas y precisas.'),
            ('Limpieza de Datos Empresariales', 'Optimización y limpieza de datos para análisis.', '2024-03-05 10:20:00', 300.00, 'Limpieza de Datos', 'images/servicios/servicio3.png', 'Inactivo', 'Garantiza la calidad y precisión de los datos para decisiones informadas.'),
            ('Automatización en Finanzas', 'Automatización de reportes financieros.', '2024-03-05 10:30:00', 450.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo', 'Automatiza procesos financieros para mayor eficiencia y control.'),
            ('Chatbot para Reservas', 'Sistema automatizado de reservas con chatbot.', '2024-03-05 10:40:00', 650.00, 'Chatbots', 'images/servicios/servicio3.png', 'Inactivo', 'Facilita la gestión de reservas y reduce la carga de trabajo.'),
            ('Normalización de Datos', 'Corrección y estructuración de bases de datos.', '2024-03-05 10:50:00', 250.00, 'Limpieza de Datos', 'images/servicios/servicio1.png', 'Activo', 'Estandariza y organiza datos para un análisis más eficiente.'),
            ('Automatización de Facturación', 'Automatización de emisión de facturas y recibos.', '2024-03-05 11:00:00', 550.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo', 'Agiliza la emisión de facturas y reduce errores manuales.'),
            ('Chatbot para Soporte Técnico', 'Asistente virtual para resolución de incidencias.', '2024-03-05 11:10:00', 800.00, 'Chatbots', 'images/servicios/servicio2.png', 'Inactivo', 'Ofrece soporte técnico inmediato y reduce tiempos de espera.'),
            ('Depuración de Datos Duplicados', 'Eliminación de registros duplicados en bases de datos.', '2024-03-05 11:20:00', 280.00, 'Limpieza de Datos', 'images/servicios/servicio1.png', 'Activo', 'Elimina duplicados para mejorar la calidad de los datos.'),
            ('Automatización de Marketing', 'Automatización de campañas de email y redes sociales.', '2024-03-05 11:30:00', 600.00, 'Automatizacion', 'images/servicios/servicio4.png', 'Activo', 'Optimiza campañas de marketing y aumenta la conversión.')
        ]
                
        # Insertar los servicios en la base de datos sin depender de los elementos seleccionados
        with connection.cursor() as cursor:
            for servicio in servicios:
                cursor.execute("""
                    INSERT INTO servicios_servicio (nombre, descripcion, fecha_publicacion, costo_base, categoria, imagen, estado, ventajas)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, servicio)

        self.message_user(request, "Los servicios fueron insertados correctamente.")
        
    poblar_servicios.short_description = "Poblar la base de datos con servicios predeterminados"
