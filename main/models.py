from django.db import models

# Create your models here.
class stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao

class reserva(models.Model):
    cnpj = models.CharField(max_length=11)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=150)
    stand = models.ForeignKey(stand, on_delete=models.CASCADE)
    quitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_empresa