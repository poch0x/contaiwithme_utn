from django.db import models

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    direccion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_empresa
    