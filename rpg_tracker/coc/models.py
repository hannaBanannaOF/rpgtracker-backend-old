from django.db import models
from rpg_tracker.core.models import FichaBase

# Create your models here.
class FichaCOC(FichaBase):
    age = models.IntegerField(verbose_name='Idade', blank=False, null=False)
    sex = models.CharField(verbose_name='Sexo', blank=False, null=False, max_length=50)
    birthplace = models.CharField(verbose_name='Local de nascimento', blank=False, null=False, max_length=50)
    residence = models.CharField(verbose_name='Residência', blank=False, null=False, max_length=50)

    def __str__(self):
        return '{0} ({1})'.format(self.nome_personagem, self.jogador)

    class Meta:
        verbose_name = 'ficha'
        verbose_name_plural = 'fichas'