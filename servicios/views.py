from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from servicios.models import Servicio
from django.http import JsonResponse


@login_required
def index(request):
    user = request.user
    return render(request, "servicios/index.html", {user: user}) 


@login_required
def get_costo_base(request, servicio_id):
    try:
        servicio = Servicio.objects.get(id=servicio_id)
        return JsonResponse({'costo_base': servicio.costo_base})
    except Servicio.DoesNotExist:
        return JsonResponse({'error': 'Servicio no encontrado'}, status=404)
    

@login_required
def get_servicios(request):
    servicios = Servicio.objects.all().values("id", "nombre", "descripcion", "costo_base", "imagen", "ventajas")
    return render(request, "base.html", {"servicios": servicios})


def obtener_servicios_json(request):
    servicios = Servicio.objects.all().values("id", "nombre", "descripcion", "costo_base", "imagen", "ventajas")
    return JsonResponse(list(servicios), safe=False)


def detalle_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    return render(request, 'servicios/detalle_servicio.html', {'servicio': servicio})
