from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from .forms import ReservaForm
from .models import Reserva
from users.permissions import GerentePermission

class ReservasListView(GerentePermission, LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "main/Listagem.html"
    paginate_by = 5

    def get_queryset(self):
        return Reserva.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_reservas'] = Reserva.objects.count()
        return context

class ReservaCreateView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin,generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
    template_name = "main/reservas-create.html"
    success_message = "Reserva criada com sucesso"



class ReservaDeleteView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("main:Listagem")
    success_message = "Reserva deletada com sucesso"


class ReservaDetailView(GerentePermission, LoginRequiredMixin, generic.DetailView):
    model = Reserva


class ReservaUpdateView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
    template_name = "main/reservas-create.html"
    success_message = "Reserva atualizada com sucesso"

