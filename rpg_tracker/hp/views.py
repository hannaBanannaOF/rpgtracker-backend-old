from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rpg_tracker.core.decorators import can_see_ficha, only_superuser
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from rpg_tracker.hp import models
# Create your views here.

class FichaDetailView(DetailView):
    model = models.FichaHP
    template_name = 'ficha_hp.html'
    context_object_name = 'ficha'

class FolioUniversitasListView(ListView):
    model = models.CategoriaFolioUniversitas
    template_name = 'folio_universitas.html'
    context_object_name = 'categorias'

    ficha = None

    def get(self, request, *args, **kwargs):
        self.ficha = models.FichaHP.objects.get(pk=kwargs.get('pk')) if kwargs.get('pk') is not None else None
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(FolioUniversitasListView, self).get_context_data(**kwargs)
        ctx['ficha'] = self.ficha
        ctx['qtde_total_cartas'] = models.CartaFolioUniversitas.objects.count()
        return ctx

class FolioUniversitasCartasListView(ListView):
    model = models.CartaFolioUniversitas
    template_name = 'folio_universitas_cartas.html'
    context_object_name = 'cartas'

    categoria = ""

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(categoria__pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        self.categoria = get_object_or_404(models.CategoriaFolioUniversitas, pk=kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['categoria'] = self.categoria
        return ctx

ficha = login_required(can_see_ficha(FichaDetailView.as_view(), 'hp'))
folio_universitas = login_required(FolioUniversitasListView.as_view())
folio_universitas_ficha = login_required(can_see_ficha(FolioUniversitasListView.as_view(), 'hp'))
folio_universitas_cartas = login_required(FolioUniversitasCartasListView.as_view())