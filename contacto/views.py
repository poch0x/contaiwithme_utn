from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contacto.forms import ConsultaForm


class Contacto(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ConsultaForm
    success_url = 'mensaje_enviado'
    
    def form_valid(self, form):
        
        # Imprimir los datos del formulario en la consola
        print("Datos del formulario que se enviarán:")
        print(form.cleaned_data)
        
        form.save()
        form.send_mail()
        return super().form_valid(form)
    

class MensajeEnviado(View):
    
    template = 'contacto/mensaje_enviado.html'
      
    def get(self, request):
        params = {}
        params['mensaje'] = 'Mensaje enviado con éxito'
        return render(request, self.template, params)
    
