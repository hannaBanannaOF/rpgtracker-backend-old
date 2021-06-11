import django_tables2 as tables
from .models import Skills
from rpg_tracker.core.tables import BaseTable

class SkillTable(BaseTable):
    name = tables.LinkColumn('coc:skill_detail', args=[tables.A('pk')], attrs={"a":{"class":"text-decoration-none text-dark stretched-link"}, "class":"clickable"})
    absolute_value = tables.Column(verbose_name='Valor', accessor='absolute_value', orderable=False)

    class Meta(BaseTable.Meta):
        model = Skills
        exclude = ("id", "created_at", "last_modified", "base_value", )
        sequence = ("name", "absolute_value", "skill_rarity", "parent_skill", "skill_kind", )
        