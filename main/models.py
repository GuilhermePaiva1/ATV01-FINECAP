from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel
from stands.models import Stand
    
class Categoria(BaseModel):
    categoria_empresa = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)

    def __str__(self):
        return f"{self.pk} | {self.categoria_empresa}"

class Reserva(BaseModel):

    cnpj_empresa = models.CharField(
        verbose_name=_("CNPJ Empresa"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH, null=True
    )
    nome_empresa = models.CharField(
        verbose_name=_("Nome Empresa"), max_length=MAX_CHAR_FIELD_NAME_LENGTH
    )
    categoria_empresa = models.ForeignKey(Categoria, on_delete=models.CASCADE,)

    quitado = models.BooleanField(_("Quitado"), default=False)
    
    stand = models.ForeignKey(
        Stand,
        verbose_name=_("Stand"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")

    def __str__(self):
        return f"{self.pk} | {self.cnpj_empresa} | {self.quitado}"
