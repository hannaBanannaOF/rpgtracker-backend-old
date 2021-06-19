import django_tables2 as tables
from .models import Skills, Ocupation
from rpg_tracker.core.tables import BaseTable

class SkillTable(BaseTable):
    name = tables.LinkColumn('coc:skill_detail', args=[tables.A('pk')], attrs={"a":{"class":"text-decoration-none text-dark stretched-link"}, "class":"clickable"})
    absolute_value = tables.Column(verbose_name='Valor', accessor='absolute_value', orderable=False)
    
    class Meta(BaseTable.Meta):
        model = Skills
        exclude = ("id", "created_at", "last_modified", "base_value", )
        sequence = ("name", "absolute_value", "skill_rarity", "parent_skill", "skill_kind", )
        empty_text = "Nenhuma Skill encontrada!"
    
class OcupationTable(BaseTable):
    #name = tables.LinkColumn('coc:skill_detail', args=[tables.A('pk')], attrs={"a":{"class":"text-decoration-none text-dark stretched-link"}, "class":"clickable"})
    class Meta(BaseTable.Meta):
        model = Ocupation
        exclude = ("id", "created_at", "last_modified", "description")
        empty_text = "Nenhuma ocupação encontrada!"
        
        