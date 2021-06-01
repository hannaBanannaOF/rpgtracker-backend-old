from django.shortcuts import render
from django.views.generic import DetailView
from . import models
# Create your views here.

class FichaDetailView(DetailView):
    model = models.FichaCOC
    template_name = 'ficha_coc.html'
    context_object_name = 'ficha'

ficha = FichaDetailView.as_view()