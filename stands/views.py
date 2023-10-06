from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import StandForm
from .models import Stand


# Create your views here.
class StandsListView(LoginRequiredMixin, generic.ListView):
    model = Stand
    paginate_by = 5

    def get_queryset(self):
        return Stand.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_stands'] = Stand.objects.count()
        return context

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand

class StandCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand cadastrado com sucesso!"

class StandUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand atualizada com sucesso!"

class StandDeleteView(LoginRequiredMixin, views.SuccessMessageMixin, generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand deletada com sucesso"
