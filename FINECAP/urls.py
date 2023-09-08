
from django.contrib import admin
from django.urls import path
from main.views import criar_reserva, detalhe, index, listar_reserva, remover

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name="index"),
    path('reservar/', criar_reserva, name='criar_reserva'),
    path('listar_reserva/', listar_reserva, name="listar"),
    path('detalhe/<int:id>/', detalhe, name="detalhe"),
    path('remover/<int:id>/', remover, name="remover"),
]
