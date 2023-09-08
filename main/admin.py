from django.contrib import admin
from .models import reserva, stand 

# Register your models here.
@admin.register(reserva)
class reservaAdmin(admin.ModelAdmin):
    list_display = ("nome_empresa",'quitado',)
    
@admin.register(stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao','valor',)