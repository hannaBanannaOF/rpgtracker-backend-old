from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import FichaDND, RacesDND, ClasseDND, TrapsDND
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
    
def traps_1_4(request):
    return render(request, 'get_trap.html', {'lvl':'1-4', 'trap_url':reverse('dnd:get_1_4_traps'), 'danger_levels':TrapsDND.DangerKind})

def traps_5_8(request):
    return render(request, 'get_trap.html', {'lvl':'5-8', 'trap_url':reverse('dnd:get_5_8_traps'), 'danger_levels':TrapsDND.DangerKind})

def traps_9_12(request):
    return render(request, 'get_trap.html', {'lvl':'9-12', 'trap_url':reverse('dnd:get_9_12_traps'), 'danger_levels':TrapsDND.DangerKind})

def traps_13_16(request):
    return render(request, 'get_trap.html', {'lvl':'13-16', 'trap_url':reverse('dnd:get_13_16_traps'), 'danger_levels':TrapsDND.DangerKind})

def traps_17_20(request):
    return render(request, 'get_trap.html', {'lvl':'17-20', 'trap_url':reverse('dnd:get_17_20_traps'), 'danger_levels':TrapsDND.DangerKind})

def traps_1_4_get(request):
    if request.is_ajax():
        traps = TrapsDND.objects.filter(level=0).all()
        if 'danger' in request.GET and request.GET.get('danger','') != '':
            traps = traps.filter(danger=request.GET['danger']).all()
        traps = list(traps)
        if len(traps) > 0:
            return HttpResponse(json.dumps(traps[randint(0,len(traps)-1)].to_dict()))
        else:
            return HttpResponse(json.dumps({'err':'Not found!'}))
    else:
        return redirect('dnd:1_4_traps')
    
def traps_5_8_get(request):
    if request.is_ajax():
        traps = TrapsDND.objects.filter(level=1).all()
        if 'danger' in request.GET and request.GET.get('danger','') != '':
            traps = traps.filter(danger=request.GET['danger']).all()
        traps = list(traps)
        if len(traps) > 0:
            return HttpResponse(json.dumps(traps[randint(0,len(traps)-1)].to_dict()))
        else:
            return HttpResponse(json.dumps({'err':'Not found!'}))
    else:
        return redirect('dnd:5_8_traps')

def traps_9_12_get(request):
    if request.is_ajax():
        traps = TrapsDND.objects.filter(level=2).all()
        if 'danger' in request.GET and request.GET.get('danger','') != '':
            traps = traps.filter(danger=request.GET['danger']).all()
        traps = list(traps)
        if len(traps) > 0:
            return HttpResponse(json.dumps(traps[randint(0,len(traps)-1)].to_dict()))
        else:
            return HttpResponse(json.dumps({'err':'Not found!'}))
    else:
        return redirect('dnd:9_12_traps')

def traps_13_16_get(request):
    if request.is_ajax():
        traps = TrapsDND.objects.filter(level=3).all()
        if 'danger' in request.GET and request.GET.get('danger','') != '':
            traps = traps.filter(danger=request.GET['danger']).all()
        traps = list(traps)
        if len(traps) > 0:
            return HttpResponse(json.dumps(traps[randint(0,len(traps)-1)].to_dict()))
        else:
            return HttpResponse(json.dumps({'err':'Not found!'}))
    else:
        return redirect('dnd:13_16_traps')

def traps_17_20_get(request):
    if request.is_ajax():
        traps = TrapsDND.objects.filter(level=4).all()
        if 'danger' in request.GET and request.GET.get('danger','') != '':
            traps = traps.filter(danger=request.GET['danger']).all()
        traps = list(traps)
        if len(traps) > 0:
            return HttpResponse(json.dumps(traps[randint(0,len(traps)-1)].to_dict()))
        else:
            return HttpResponse(json.dumps({'err':'Not found!'}))
    else:
        return redirect('dnd:17_20_traps')