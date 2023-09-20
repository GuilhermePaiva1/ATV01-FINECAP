from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel

# Create your models here.
class Stand(BaseModel):
    localizacao = models.CharField(
        verbose_name=_("Localização"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH
    )
    valor = models.DecimalField(
        verbose_name=_("Valor"),
        decimal_places=2,
        max_digits=6
    )

    class Meta:
        verbose_name = _("Stand")
        verbose_name_plural = _("Stands")

    def __str__(self):
        return f"{self.pk} | {self.localizacao}"


class Reserva(BaseModel):

    class Categoria(models.TextChoices):
        TEC = "TECNOLOGIA", _("Tecnologia")
        AGRO = "AGRO", _("Agro Negócio")

    cnpj_empresa = models.CharField(
        verbose_name=_("CNPJ Empresa"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH, null=True
    )
    nome_empresa = models.CharField(
        verbose_name=_("Nome Empresa"), max_length=MAX_CHAR_FIELD_NAME_LENGTH
    )
    email_empresa = models.EmailField(
        verbose_name=_("E-mail"),
        max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH,
    )
    categoria_empresa = models.CharField(
        verbose_name=_("Categoria Empresa"),
        max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
        choices=Categoria.choices,
    )
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