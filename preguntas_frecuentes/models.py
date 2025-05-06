from django.db import models

class Pregunta(models.Model):
    ESTADO = (
        (1, 'Activa'),
        (2, 'Inactiva'),
    )
    
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    estado =  models.IntegerField(choices=ESTADO, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.pregunta