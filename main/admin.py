from django.contrib import admin

from . import models


# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    search_fields = ["cnpj_empresa"]
    readonly_fields = ["updated_by", "created_at"]


admin.site.register(models.Reserva, ReservaAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ["categoria_empresa"]
    readonly_fields = ["updated_by", "created_at"]

admin.site.register(models.Categoria, CategoriaAdmin)