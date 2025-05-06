from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.models import User
from servicios.models import Servicio
from django.views.decorators.csrf import csrf_exempt



@login_required
def index(request):
    user = request.user
    return render(request, "dashboard/index.html", {"user": user})


@login_required
def inicio(request):
    user = request.user
    return render(request, "dashboard/partials/_inicio.html", {"user": user})


@login_required
def perfil(request):
    if request.method == "POST":
        # Obtener el nuevo username del formulario
        nuevo_username = request.POST.get("nombre")

        # Validar que el nuevo username no esté vacío
        if nuevo_username:
            # Actualizar el username del usuario
            user = request.user
            user.username = nuevo_username
            user.save()

            # Mostrar un mensaje de éxito
            messages.success(request, "Username actualizado correctamente.")
        else:
            # Mostrar un mensaje de error si el campo está vacío
            messages.error(request, "El campo de username no puede estar vacío.")

        # Redirigir a la misma página para evitar reenvíos del formulario
        return redirect("dashboard/partials/_perfil.html")

    # Si es una solicitud GET, simplemente renderiza el template
    return render(request, "dashboard/partials/_perfil.html", {"user": request.user})


@login_required
def update_perfil(request):
    if request.method == "POST":
        user = request.user
        data = request.POST

        try:
            # Actualizar los datos del usuario
            user.first_name = data.get("first_name", user.first_name)
            user.last_name = data.get("last_name", user.last_name)
            user.email = data.get("email", user.email)

            # Si deseas actualizar el username, agrega esta línea
            nuevo_username = data.get("username")
            if nuevo_username and nuevo_username != user.username:
                # Verificar si el nuevo username ya está en uso
                if User.objects.filter(username=nuevo_username).exists():
                    return JsonResponse({"message": "El nombre de usuario ya está en uso."}, status=400)
                user.username = nuevo_username

            # Validar y guardar los cambios
            user.full_clean()  # Valida los campos del modelo
            user.save()

            return JsonResponse({"message": "Datos actualizados correctamente"})
        except ValidationError as e:
            # Capturar errores de validación del modelo
            return JsonResponse({"message": f"Error de validación: {str(e)}"}, status=400)
        except Exception as e:
            # Capturar cualquier otro error
            return JsonResponse({"message": f"Error al actualizar los datos: {str(e)}"}, status=500)

    # Si no es una solicitud POST, devolver un error
    return JsonResponse({"message": "Método no permitido"}, status=405)


@login_required
def configuracion(request):
    user = request.user
    return render(request, "dashboard/partials/_configuracion.html", {"user": user})


def servicios(request):
    return render(request, "dashboard/partials/_servicios.html")


# def listar_servicios(request):
#     servicios = Servicio.objects.all()

#     if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.GET.get("format") == "json":
#         data = [
#             {
#                 "id": servicio.id,
#                 "nombre": servicio.nombre,
#                 "descripcion": servicio.descripcion,
#                 "precio": servicio.costo_base,  # Asegúrate de que este es el campo correcto
#             }
#             for servicio in servicios
#         ]
#         return JsonResponse(data, safe=False)

#     return render(request, "dashboard/partials/_servicios.html", {"servicios": servicios})

def listar_servicios(request):
    termino = request.GET.get("termino", "")  # Obtener el término de búsqueda
    servicios = Servicio.objects.all()

    # Filtrar servicios si hay un término de búsqueda
    if termino:
        servicios = servicios.filter(nombre__icontains=termino) | servicios.filter(descripcion__icontains=termino)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.GET.get("format") == "json":
        data = [
            {
                "id": servicio.id,
                "nombre": servicio.nombre,
                "descripcion": servicio.descripcion,
                "precio": servicio.costo_base,  # Asegúrate de que este es el campo correcto
            }
            for servicio in servicios
        ]
        return JsonResponse(data, safe=False)

    return render(request, "dashboard/partials/_servicios.html", {"servicios": servicios})


def obtener_servicio(request, servicio_id):
    try:
        servicio = get_object_or_404(Servicio, id=servicio_id)
        data = {
            'id': servicio.id,
            'nombre': servicio.nombre,
            'descripcion': servicio.descripcion,
            'costo_base': float(servicio.costo_base)  # Cambia "precio" por "costo_base"
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == 'POST':
        servicio.nombre = request.POST.get('nombre')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.costo_base = request.POST.get('costo_base')
        servicio.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def eliminar_servicio(request, servicio_id):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, id=servicio_id)
        servicio.delete()
        return JsonResponse({"message": "Servicio eliminado correctamente."}, status=200)
    return JsonResponse({"error": "Método no permitido."}, status=405)


@csrf_exempt
def crear_servicio(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            costo_base = request.POST.get('costo_base')
            categoria = request.POST.get('categoria')
            estado = request.POST.get('estado')

            # Validar que los campos no estén vacíos
            if not nombre or not descripcion or not costo_base or not categoria or not estado:
                return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)

            # Crear el servicio
            servicio = Servicio.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                costo_base=costo_base,
                categoria=categoria,
                estado=estado
            )

            return JsonResponse({
                'success': True,
                'id': servicio.id,
                'nombre': servicio.nombre,
                'descripcion': servicio.descripcion,
                'costo_base': float(servicio.costo_base),
                'categoria': servicio.categoria,
                'estado': servicio.estado
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)