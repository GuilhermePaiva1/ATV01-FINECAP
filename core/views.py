from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from main.models import Reserva
from stands.models import Stand
from django.contrib.messages import views
from django.contrib import messages

# Create your views here.
class HomeView(LoginRequiredMixin, views.SuccessMessageMixin, generic.TemplateView):
    template_name = "pages/home.html"
    success_message = "Login realizado com sucesso"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_reservas'] = Reserva.objects.count()
        context['num_stands'] = Stand.objects.count()
        return context
        
    def form_valid(self, form):
        # Faça a autenticação do usuário aqui, se necessário
        # Por exemplo, você pode usar o método 'form.get_user()' para obter o usuário autenticado

        # Defina a mensagem de sucesso usando 'messages.success'
        messages.success(self.request, 'Você foi autenticado com sucesso!')

        return super().form_valid(form)