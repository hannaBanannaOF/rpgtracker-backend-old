from rpg_tracker.core.models import MesaBase
from django.contrib import admin
from .models import FichaCOC, Ocupation, Skills, SkillsOnFicha, Ammo, Weapons, WeaponsInFicha, MesaCOC, PulpTalents
# Register your models here.

class FichaCOCAdmin(admin.ModelAdmin):
    list_filter = ('jogador',)

class SkillOnFichaAdmin(admin.ModelAdmin):
    list_filter = ('ficha',)

admin.site.register(FichaCOC, FichaCOCAdmin)
admin.site.register(SkillsOnFicha, SkillOnFichaAdmin)
admin.site.register([Ocupation, Skills, Ammo, Weapons, WeaponsInFicha, MesaCOC, PulpTalents])