from django.db import models
from django.utils.html import format_html
from django.utils import timezone

class Servicio(models.Model):
    AUTOMATIZACION = 'Automatizacion'
    CHATBOTS = 'Chatbots'
    LIMPIEZA_DATOS = 'Limpieza de Datos'
    
    CATEGORIA_SERVICIO = (
        (AUTOMATIZACION, 'Automatizacion'),
        (CHATBOTS, 'Chatbots'),
        (LIMPIEZA_DATOS, 'Limpieza de Datos'),
    )
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()  # Cambiado a TextField para mayor flexibilidad
    fecha_publicacion = models.DateTimeField("Fecha de publicacion", default=timezone.now)  # Valor por defecto
    costo_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Usar DecimalField para precios
    categoria = models.CharField(max_length=20, choices=CATEGORIA_SERVICIO, default=None)  # Aumentado el max_length y corregido el default
    imagen = models.ImageField(upload_to="servicios/%Y/%m/%d", blank=True, null=True)  # Corregido el nombre de la carpeta
    
    # Estado del servicio (activo/inactivo)
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_CHOICES = (
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=ACTIVO)
    
    ventajas = models.TextField(blank=True, null=True)  # Nuevo campo para ventajas

    def __str__(self):
        return self.nombre
    
    def imagen_html(self):
        if self.imagen and self.imagen.storage.exists(self.imagen.name):
            print(f"URL de la imagen: {self.imagen.url}")
            return format_html('<img src="{}" width="100" height="40" />', self.imagen.url)
        print("Imagen no encontrada")
        return "No image"

    
    imagen_html.short_description = 'Imagen'
    
    
    