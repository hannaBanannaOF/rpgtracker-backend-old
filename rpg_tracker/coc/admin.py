from django.contrib import admin
from .models import FichaCOC, Ocupation, Skills, SkillsOnFicha, Ammo, Weapons, WeaponsInFicha
# Register your models here.
admin.site.register([FichaCOC, Ocupation, Skills, SkillsOnFicha, Ammo, Weapons, WeaponsInFicha])