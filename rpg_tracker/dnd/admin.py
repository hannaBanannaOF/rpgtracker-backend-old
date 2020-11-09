from django.contrib import admin
from .models import FichaDND, RacesDND, RaceTraitsDND, LanguagesDND, ClasseDND, ClassesFichaDND
# Register your models here.
admin.site.register([FichaDND, RacesDND, RaceTraitsDND, LanguagesDND, ClasseDND, ClassesFichaDND])