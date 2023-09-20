from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ReservaForm
from .models import Reserva
# Create your views here.

#def index(request):
#    return render(request, 'index.html')
class HomeView(generic.TemplateView):
    template_name = "main/index.html"

#def listar_reserva(request):
 #   reservas = reserva.objects.all() 
  #  context = {'reservas': reservas}
   # return render(request, 'Listagem.html', context)
class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "main/Listagem.html"

#def criar_reserva(request):
#    if request.method == "POST":
#
#       form = reservaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('listar')
#    else: 
#        form = reservaForm()
#
#    return render(request, 'reserva.html', {'form': form})
class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
    template_name = "main/reservas-create.html"

#def remover(request, id):
#    reserva_obj = get_object_or_404(reserva, id=id)  
#    reserva_obj.delete()
#    return redirect('listar')
class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("main:Listagem")

#def detalhe(request, id):
#    reserva_obj = get_object_or_404(reserva, id=id) 
#    context = {'reserva': reserva_obj}
#    return render(request, 'detalhe_reserva.html', context)
class ReservaDetailView(generic.DetailView):
    model = Reserva

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("main:Listagem")
