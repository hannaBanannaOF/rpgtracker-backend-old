from django import forms
from .models import Skills, Ocupation

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('name', 'base_value', 'skill_rarity', 'parent_skill', 'skill_kind',)

class OcupationForm(forms.ModelForm):
    class Meta:
        model = Ocupation
        fields = ("name",)