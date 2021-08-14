from django.shortcuts import render
from rpg_tracker.core.models import FichaBase

# Create your views here.
def perfil(request):
    ctx = {}
    if request.user.is_superuser:
        ctx['fichas'] = FichaBase.objects.all()
    return render(request, 'perfil.html', ctx)