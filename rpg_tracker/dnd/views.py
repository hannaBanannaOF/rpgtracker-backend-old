from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import FichaDND, RacesDND, ClasseDND
from django.views.generic import ListView, DetailView
from django.templatetags.static import static
import json
from random import randint
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

def get_deck_gm_crit(request):
    return render(request, 'get_deck.html', {'action':'gm_get_deck', 'loader':static('img/loader.gif')})

def get_deck_player_crit(request):
    return render(request, 'get_deck.html', {'action':'player_get_deck', 'loader':static('img/loader.gif')})

def get_deck_fail(request):
    return render(request, 'get_deck.html', {'action':'fail_get_deck', 'loader':static('img/loader.gif')})


def deck_gm_crit_card(request):
    if request.is_ajax():
        img = static('img/decks/crit_gm/{0}.png'.format(str(randint(1,52))))
        return HttpResponse(json.dumps({'img':img}))
    else:
        return redirect('dnd:gm_crit_deck')

def deck_player_crit_card(request):
    if request.is_ajax():
        img = static('img/decks/crit_player/{0}.png'.format(str(randint(1,52))))
        return HttpResponse(json.dumps({'img':img}))
    else:
        return redirect('dnd:player_crit_deck')

def deck_fail_card(request):
    if request.is_ajax():
        img = static('img/decks/fumble/{0}.png'.format(str(randint(1,52))))
        return HttpResponse(json.dumps({'img':img}))
    else:
        return redirect('dnd:fail_deck')