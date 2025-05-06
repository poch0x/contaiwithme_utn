from django.shortcuts import render
from servicios.models import Servicio

def home(request):
    
    # servicios = [
    #     {"nombre": "Optimización", "descripcion": "Optimiza procesos empresariales con inteligencia artificial.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+1"},
    #     {"nombre": "Automatización", "descripcion": "Automatiza tareas repetitivas y mejora la eficiencia.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+2"},
    #     {"nombre": "Análisis", "descripcion": "Obtén análisis detallados con nuestras herram,ientas avanzadas.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+3"},
    #     {"nombre": "Seguridad", "descripcion": "Protege tu información y la de tus clientes con nuestros servicios de seguridad.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+4"},
    #     {"nombre": "Desarrollo", "descripcion": "Desarrolla aplicaciones web y móviles con nosotros.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+5"},
    #     {"nombre": "Consultoría", "descripcion": "Recibe asesoría de expertos en tecnología.", "imagen": "https://via.placeholder.com/300x200.png?text=Imagen+6"},
    # ]
    
    servicios = Servicio.objects.all().values("id", "nombre", "descripcion", "costo_base", "imagen")
    return render(request, "base.html", {"servicios": servicios})
    
def prueba(request):
    return render(request, "layout.html")


