from rpg_tracker.core.models import MesaBase
from django.contrib import admin
from .models import FichaCOC, Ocupation, Skills, SkillsOnFicha, Ammo, Weapons, WeaponsInFicha, MesaCOC, PulpTalents
# Register your models here.
admin.site.register([FichaCOC, Ocupation, Skills, SkillsOnFicha, Ammo, Weapons, WeaponsInFicha, MesaCOC, PulpTalents])