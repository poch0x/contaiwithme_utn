from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contrato, LogActividad
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Contrato)
def registrar_actividad_en_log(sender, instance, **kwargs):
    """
    Registra una actividad en el log cada vez que se actualiza un contrato.
    """
    if instance.pk:  # Verifica si el contrato ya existe (no es una creación nueva)
        mensaje = (
            f"El contrato {instance.id} fue actualizado. "
            f"Cliente: {instance.cliente.nombre_empresa}, "
            f"Servicio: {instance.servicio.nombre}, "
            f"Costo Total: {instance.costo_total}, "
            f"Fecha Inicio: {instance.fecha_inicio}, "
            f"Fecha Fin: {instance.fecha_fin}."
        )

        # Registrar en el modelo LogActividad
        LogActividad.objects.create(contrato=instance, mensaje=mensaje)

        # Registrar en el log del sistema (opcional)
        logger.info(mensaje)