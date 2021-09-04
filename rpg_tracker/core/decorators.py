from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rpg_tracker.coc.models import FichaCOC
from rpg_tracker.hp.models import FichaHP

def can_see_ficha(function, type):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        can_see = False
        if(type == 'coc'):
            ficha = get_object_or_404(FichaCOC, pk=kwargs['pk'])
        elif(type == 'hp'):
            ficha = get_object_or_404(FichaHP, pk=kwargs['pk'])
        else:
            raise PermissionDenied
        for x in ficha.mesas_jogadas.all():
            if x.is_player_in_mesa(request.user):
                can_see = True
                break
            can_see = x.mesa.is_mestre(request.user)
            if can_see:
                break
        if not can_see:
            can_see = ficha.jogador == request.user
        #if request.user.is_staff:
        if can_see or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper

def only_superuser(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper