from django.forms import ModelForm
from django import forms
from .models import Stand, Reserva

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj_empresa' : forms.TextInput(attrs={'class': 'form-control',"placeholder": "CNPJ da empresa", }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control',"placeholder": "Nome da empresa", }),
            'email_empresa' : forms.EmailInput(attrs={'class': 'form-control',"placeholder": "Email da empresa", }),
            'categoria_empresa' : forms.Select(attrs={'class': 'form-control', }),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stand': forms.Select(attrs={'class': 'form-control', }),
        }