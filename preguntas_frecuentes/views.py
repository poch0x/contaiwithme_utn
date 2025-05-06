from django.http import JsonResponse
from django.shortcuts import render
from preguntas_frecuentes.models import Pregunta

def preguntas_frecuentes(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Si es una solicitud AJAX, devolver JSON
        preguntas = Pregunta.objects.all().order_by('-fecha_creacion').values("pregunta", "respuesta")
        return JsonResponse(list(preguntas), safe=False)
    else:
        # Si no es AJAX, renderizar el template normalmente
        return render(request, "preguntas_frecuentes.html")