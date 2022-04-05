from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rpg_tracker.coc.models import FichaCOC
from rpg_tracker.hp.models import FichaHP

def can_see_ficha(function, type):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if(type == 'coc'):
            ficha = get_object_or_404(FichaCOC, pk=kwargs['pk'])
        elif(type == 'hp'):
            ficha = get_object_or_404(FichaHP, pk=kwargs['pk'])
        else:
            raise PermissionDenied("Você não tem permissão de visualizar essa ficha!")
        if (ficha.mesa and (ficha.mesa.is_mestre(request.user) or ficha.jogador == request.user or request.user.is_superuser)):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied("Você não tem permissão de visualizar essa ficha!")
    return wrapper

def only_superuser(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrapper