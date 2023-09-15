from django.shortcuts import render, get_object_or_404, redirect
from .models import reserva, stand
from .forms import reservaForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def listar_reserva(request):
    reservas = reserva.objects.all() 
    context = {'reservas': reservas}
    return render(request, 'main/Listagem.html', context)

def criar_reserva(request):
    if request.method == "POST":

        form = reservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else: 
        form = reservaForm()

    return render(request, 'main/reserva.html', {'form': form})

def remover(request, id):
    reserva_obj = get_object_or_404(reserva, id=id)  
    reserva_obj.delete()
    return redirect('listar')

def detalhe(request, id):
    reserva_obj = get_object_or_404(reserva, id=id) 
    context = {'reserva': reserva_obj}
    return render(request, 'main/detalhe_reserva.html', context)

class ReservaUpdateView(generic.UpdateView):
    model = reserva
    form_class = reservaForm
    success_url = reverse_lazy("main/Listagem.html")
    template_name = "main/Listagem.html"

