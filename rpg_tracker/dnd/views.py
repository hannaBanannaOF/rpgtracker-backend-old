from django.shortcuts import render, get_object_or_404
from .models import FichaDND, RacesDND
from django.views.generic import ListView, DetailView
# Create your views here.

class RaceDNDListView(ListView):
    model = RacesDND
    template_name = 'racas_dnd.html'
    context_object_name = 'racas'

class RaceDNDDetailView(DetailView):
    model = RacesDND
    template_name = 'racas_details_dnd.html'
    context_object_name = 'raca'

def ficha_detalhe(request, pk):
    f = get_object_or_404(FichaDND, pk=pk)
    return render(request, 'ficha_details_dnd.html', {'ficha':f.to_dict()})