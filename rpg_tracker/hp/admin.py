from django.contrib import admin
from .models import Varinha, EspecializacoesCustomizadasPlayer, PericiasEspecializacoes, PericiasEspecializacoesFicha, FichaHP, Mesa

admin.site.register([Varinha, EspecializacoesCustomizadasPlayer, PericiasEspecializacoes, PericiasEspecializacoesFicha, FichaHP, Mesa])
# Register your models here.
