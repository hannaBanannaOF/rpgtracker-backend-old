from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import FichaCOC, MesaCOC

def can_see_ficha(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        can_see = False
        ficha = get_object_or_404(FichaCOC, pk=kwargs['pk'])
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
        if can_see or request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper