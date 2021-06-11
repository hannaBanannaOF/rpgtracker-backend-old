from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import DetailView
from django_tables2 import SingleTableView, LazyPaginator
from . import models
from . import tables
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
class FichaDetailView(DetailView):
    model = models.FichaCOC
    template_name = 'ficha_coc.html'
    context_object_name = 'ficha'

class SkillDetailView(DetailView):
    model = models.Skills
    template_name = 'skill_detail.html'
    context_object_name = 'skill'

    def get(self, request, *args, **kwargs):
        response = super(SkillDetailView, self).get(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        ctx = super(SkillDetailView, self).get_context_data(**kwargs)
        ctx['form'] = forms.SkillForm(instance=self.object)
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
    template_name = 'skills_coc.html'
    paginator_class = LazyPaginator

ficha = login_required(FichaDetailView.as_view())
skill_list = login_required(SkillListView.as_view())
skill_detail = login_required(SkillDetailView.as_view())