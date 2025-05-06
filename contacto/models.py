from django.db import models
from datetime import datetime
from django.utils.html import format_html


class Consulta(models.Model): 

    CONTESTADA = 'Contestada'
    NOCONTESTADA = 'No contestada'
    ENPROCESO = 'En proceso'
    
    ESTADOS = (
        (CONTESTADA, 'Contestada'),
        (NOCONTESTADA, 'No contestada'),
        (ENPROCESO, 'En proceso'),
    )
    
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(max_length=100, blank=False, null=False)
    mail = models.EmailField(max_length=50, blank=True, null=True)
    estado_respuesta = models.CharField(max_length=15, choices=ESTADOS, default=NOCONTESTADA)
    celular = models.CharField(max_length=20, blank=True, null=True) 
    fecha = models.DateTimeField(default=datetime.now, blank=True, editable=True)
    
    def __str__(self):
        return self.nombre
    
    def estado_de_respuesta(self):
        if self.estado_respuesta == 'Contestada':
            return format_html('<span style="background-color:#0a0; color:#fff; padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'No contestada':
            return format_html('<span style="background-color:#a00; color:#fff; padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'En proceso':
            return format_html('<span style="background-color:#f0b203; color:#000; padding:5px;">{}</span>', self.estado_respuesta)


class Respuesta(models.Model): 
    
    consulta = models.ForeignKey(Consulta(), blank=True, null=True, on_delete=models.CASCADE)
    respuesta = models.TextField(max_length=100, blank=False, null=False)
    # mail = models.EmailField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(default=datetime.now, blank=True, editable=True)

    def create_mensaje(self, ):
        consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = 'Contestada'
        consulta_cambio_estado.save()
    # LOGICA DE ENVIO DE MAIL
    
    
    
    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
            super(Respuesta, self).save(force_update=force_update)