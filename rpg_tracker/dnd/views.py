from django.shortcuts import render, get_object_or_404
from .models import FichaDND
# Create your views here.
def ficha_detalhe(request, pk):
    f = get_object_or_404(FichaDND, pk=pk)
    return render(request, 'ficha_details_dnd.html', {'ficha':f.to_dict()})