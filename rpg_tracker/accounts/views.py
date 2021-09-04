from rpg_tracker.core.decorators import only_superuser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rpg_tracker.core.models import FichaBase

# Create your views here.
@login_required
def fichas(request):
    ctx = {}
    if request.user.is_superuser:
        ctx['fichas'] = FichaBase.objects.all()
    return render(request, 'perfil.html', ctx)