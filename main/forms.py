from django.forms import ModelForm
from django import forms
from .models import Stand, Reserva

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        widgets = {
            'cnpj_empresa' : forms.TextInput(attrs={'class': 'form-control',"placeholder": "CNPJ da empresa", }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control',"placeholder": "Nome da empresa", }),
            'categoria_empresa' : forms.Select(attrs={'class': 'form-control', }),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stand': forms.Select(attrs={'class': 'form-control', }),

        }

        fields = (
            'cnpj_empresa',
            'nome_empresa',
            'categoria_empresa',
            'quitado',
            'stand',
        )