from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
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
            raise PermissionDenied
        if (ficha.mesa and (ficha.mesa.is_mestre(request.user) or ficha.jogador == request.user or request.user.is_superuser)):
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

def has_nickname(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.nickname is None or request.user.nickname == "":
            redirect(reverse("accounts:user-info", request.user.pk))
        return function(request, *args, **kwargs)
    return wrapper