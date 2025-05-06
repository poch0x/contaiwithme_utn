from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):
    
    captcha = CaptchaField()
    
    class Meta:
        model = Consulta
        fields = ['nombre',
                  'descripcion',
                  'mail',
                  'celular',
            
        ]
        # labels = {
        #     'nombre': 'Nombre',
        #     'descripcion': 'Consulta',
        #     'mail': 'Mail',
        #     'celular': 'Celular',
        # }
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        #     'mail': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'celular': forms.TextInput(attrs={'class': 'form-control'}),
        # }
        
    def send_mail(self,):
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        mail = self.cleaned_data['mail']
        celular = self.cleaned_data['celular']
        
        # LOGICA DE ENVIO DE MAIL
        