from django.urls import reverse
from django.views.generic import DetailView
from django_tables2 import SingleTableView, LazyPaginator
from . import models
from . import tables
from . import forms
from rpg_tracker.core.decorators import can_see_ficha
from django.contrib.auth.decorators import login_required
from .serializers import FichaCOCSerializer
from hbcommons.views import QueryStringRetriveApiView

# Create your views here.
class FichaDetails(QueryStringRetriveApiView):
    queryset = models.FichaCOC
    serializer_class = FichaCOCSerializer
    query_param_fields=["pk"]


############################ NO API CALLS ###############################

class FichaDetailView(DetailView):
    model = models.FichaCOC
    template_name = 'ficha_coc.html'
    context_object_name = 'ficha'

class SkillDetailView(DetailView):
    model = models.Skills
    template_name = 'coc_detail.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        response = super(SkillDetailView, self).get(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        ctx = super(SkillDetailView, self).get_context_data(**kwargs)
        ctx['form'] = forms.SkillForm(instance=self.object)
        ctx['post_url'] = reverse("coc:skill_detail", args=[self.get_object().pk])
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = forms.SkillForm(request.POST or None, instance=self.get_object())
        if form.is_valid():
            self.object = form.save()
        else:    
            self.object = self.get_object()
        ctx = self.get_context_data(object=self.object)
        ctx['form'] = forms.SkillForm(instance=self.object)
        return self.render_to_response(ctx)

class SkillListView(SingleTableView):
    model = models.Skills
    table_class = tables.SkillTable
    template_name = 'listings_coc.html'
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        ctx = super(SkillListView, self).get_context_data(**kwargs)
        ctx['page_title'] = "Inverstigator skills"

        return ctx

class OcupationListView(SingleTableView):
    model = models.Ocupation
    table_class = tables.OcupationTable
    template_name = 'listings_coc.html'
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        ctx = super(OcupationListView, self).get_context_data(**kwargs)
        ctx['page_title'] = "Ocupations"

        return ctx

ficha = login_required(can_see_ficha(FichaDetailView.as_view(), 'coc'))
skill_list = login_required(SkillListView.as_view())
skill_detail = login_required(SkillDetailView.as_view())
ocupation_list = login_required(OcupationListView.as_view())