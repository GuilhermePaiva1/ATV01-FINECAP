from django import forms
from decimal import Decimal

from stands.models import Stand


class StandForm(forms.ModelForm):

    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Localização do stand",
        })
    )
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "money form-control", 
            "placeholder": "Valor do stand",
})
)

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return valor.replace(",", ".")

    class Meta:
        model = Stand
        fields = (
            "localizacao",
            "valor",
        )
