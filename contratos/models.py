from django.db import models
from django.utils.timezone import now

from clientes.models import Cliente
from servicios.models import Servicio


class Contrato(models.Model):

    ESTADOS_CONTRATO = [
        ('vigente', 'Vigente'),
        ('pronto_a_vencer', 'Pronto a Vencer'),
        ('vencido', 'Vencido'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS_CONTRATO, default='vigente')

    def actualizar_estado(self):
        """Método para actualizar el estado del contrato basado en las fechas."""
        hoy = now().date()
        dias_restantes = (self.fecha_fin - hoy).days

        if dias_restantes < 0:
            return 'vencido'
        elif dias_restantes <= 10:  # Últimos 10 días antes de la fecha_fin
            return 'pronto_a_vencer'
        return 'vigente'

    def save(self, *args, **kwargs):
        """Actualiza el estado antes de guardar, sin llamar save() recursivamente."""
        self.estado = self.actualizar_estado()
        super().save(*args, **kwargs)  # ← Ahora solo llamamos save() una vez

    def __str__(self):
        return f"Contrato {self.id} - {self.cliente.nombre_empresa} ({self.get_estado_display()})"


class LogActividad(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='logs')
    mensaje = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.id} - Contrato {self.contrato.id}"
