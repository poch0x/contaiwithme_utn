from django.contrib import admin
from .models import Pregunta

# Acción personalizada para poblar la base de datos con preguntas frecuentes
def poblar_preguntas_frecuentes(modeladmin, request, queryset):
    # Datos de las preguntas frecuentes
    preguntas_frecuentes = [
        {
            "pregunta": "¿Cómo puede ayudarme la automatización de procesos en mi empresa?",
            "respuesta": "La automatización de procesos reduce el tiempo en tareas repetitivas, minimiza errores y mejora la eficiencia operativa, permitiéndote centrarte en actividades estratégicas.",
            "estado": 1,
        },
        {
            "pregunta": "¿Qué beneficios ofrece un chatbot en la atención al cliente?",
            "respuesta": "Un chatbot con inteligencia artificial puede responder consultas en tiempo real, mejorar la experiencia del cliente y reducir la carga de trabajo del equipo de soporte.",
            "estado": 1,
        },
        {
            "pregunta": "¿Cómo se garantiza la seguridad de mis datos al usar sus servicios?",
            "respuesta": "Implementamos protocolos de seguridad avanzados, encriptación de datos y cumplimiento con normativas de protección de datos para garantizar la privacidad y seguridad de la información.",
            "estado": 1,
        },
        {
            "pregunta": "¿Qué tipo de empresas pueden beneficiarse de sus servicios?",
            "respuesta": "Nuestros servicios están diseñados para empresas de todos los tamaños que deseen optimizar sus operaciones mediante inteligencia artificial, desde startups hasta grandes corporaciones.",
            "estado": 1,
        },
        {
            "pregunta": "¿Cuál es el proceso para contratar un chatbot personalizado?",
            "respuesta": "El proceso incluye una consulta inicial, desarrollo a medida según tus necesidades y pruebas antes de la implementación final.",
            "estado": 1,
        },
        {
            "pregunta": "¿Cómo puedo saber qué servicio de IA es el más adecuado para mi empresa?",
            "respuesta": "Te ofrecemos una consulta gratuita para evaluar tus necesidades y recomendarte la mejor solución en función de tus objetivos y presupuesto.",
            "estado": 1,
        },
        {
            "pregunta": "¿Qué ventajas tiene la limpieza y normalización de datos?",
            "respuesta": "La limpieza de datos mejora la calidad y precisión de la información, lo que permite tomar decisiones más informadas y evitar errores en análisis o reportes.",
            "estado": 1,
        },
        {
            "pregunta": "¿Puedo integrar sus soluciones de automatización con mis sistemas actuales?",
            "respuesta": "Sí, nuestras soluciones son compatibles con diversas plataformas y pueden integrarse sin problemas con tus sistemas existentes mediante API u otras herramientas.",
            "estado": 1,
        },
        {
            "pregunta": "¿Ofrecen soporte técnico después de la implementación?",
            "respuesta": "Sí, brindamos soporte continuo para garantizar el correcto funcionamiento de nuestros servicios y resolver cualquier duda o inconveniente que pueda surgir.",
            "estado": 1,
        }
    ]


    # Crear las preguntas en la base de datos
    for pregunta_data in preguntas_frecuentes:
        Pregunta.objects.create(
            pregunta=pregunta_data["pregunta"],
            respuesta=pregunta_data["respuesta"],
            estado=pregunta_data["estado"],
        )

    # Mensaje de confirmación
    modeladmin.message_user(request, "Base de datos poblada con preguntas frecuentes exitosamente.")

# Personalizar la clase del admin para Pregunta
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'estado', 'fecha_creacion')  # Campos a mostrar en la lista
    actions = [poblar_preguntas_frecuentes]  # Agregar la acción personalizada

# Registrar el modelo Pregunta con la clase personalizada
admin.site.register(Pregunta, PreguntaAdmin)