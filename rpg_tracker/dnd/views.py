from django.shortcuts import render, get_object_or_404
from .models import FichaDND, RacesDND, ClasseDND
from django.views.generic import ListView, DetailView
# Create your views here.

class RaceDNDListView(ListView):
    model = RacesDND
    template_name = 'racas_dnd.html'
    context_object_name = 'racas'

class ClasseDNDListView(ListView):
    model = ClasseDND
    template_name = 'classes_dnd.html'
    context_object_name = 'classes'

class RaceDNDDetailView(DetailView):
    model = RacesDND
    template_name = 'racas_details_dnd.html'
    context_object_name = 'raca'

class ClasseDNDDetailView(DetailView):
    model = ClasseDND
    template_name = 'classes_details_dnd.html'
    context_object_name = 'classe'

def ficha_detalhe(request, pk):
    f = get_object_or_404(FichaDND, pk=pk)
    return render(request, 'ficha_details_dnd.html', {'ficha':f.to_dict()})