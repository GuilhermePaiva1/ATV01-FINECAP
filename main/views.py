from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from .forms import ReservaForm
from .models import Reserva

class HomeView(generic.TemplateView):
    template_name = "main/index.html"


class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "main/Listagem.html"


class ReservaCreateView(views.SuccessMessageMixin,generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
    template_name = "main/reservas-create.html"
    success_message = "Reserva criada com sucesso"



class ReservaDeleteView(views.SuccessMessageMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("main:Listagem")
    success_message = "Reserva deletada com sucesso"


class ReservaDetailView(generic.DetailView):
    model = Reserva


class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
    template_name = "main/reservas-create.html"
    success_message = "Reserva atualizada com sucesso"

