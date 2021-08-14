from django.contrib.auth.decorators import login_required
from rpg_tracker.core.decorators import can_see_ficha
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from rpg_tracker.hp import models
# Create your views here.

class FichaDetailView(DetailView):
    model = models.FichaHP
    template_name = 'ficha_hp.html'
    context_object_name = 'ficha'

class FolioUniversitasListView(ListView):
    model = models.CategoriaFolioUniversitas
    template_name = 'folio_universitas.html'
    context_object_name = 'categorias'

ficha = login_required(can_see_ficha(FichaDetailView.as_view(), 'hp'))
folio_universitas = login_required(FolioUniversitasListView.as_view())