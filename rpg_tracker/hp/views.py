from django.contrib.auth.decorators import login_required
from rpg_tracker.core.decorators import can_see_ficha
from django.shortcuts import render
from django.views.generic.detail import DetailView
from rpg_tracker.hp import models
# Create your views here.

class FichaDetailView(DetailView):
    model = models.FichaHP
    template_name = 'ficha_hp.html'
    context_object_name = 'ficha'

ficha = login_required(can_see_ficha(FichaDetailView.as_view(), 'hp'))