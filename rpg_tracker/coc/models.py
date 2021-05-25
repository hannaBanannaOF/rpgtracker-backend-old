from django.db import models
from rpg_tracker.core.models import FichaBase, AbstractBaseModel
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class FichaCOC(FichaBase):
    age = models.IntegerField(verbose_name='Idade', blank=False, null=False)
    sex = models.CharField(verbose_name='Sexo', blank=False, null=False, max_length=50)
    birthplace = models.CharField(verbose_name='Local de nascimento', blank=False, null=False, max_length=50)
    residence = models.CharField(verbose_name='Residência', blank=False, null=False, max_length=50)
    strength = models.IntegerField(verbose_name='Força', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    constitution = models.IntegerField(verbose_name='Constituição', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    size = models.IntegerField(verbose_name='Tamanho', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    dexterity = models.IntegerField(verbose_name='Destreza', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    appearence = models.IntegerField(verbose_name='Aparência', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    inteligence = models.IntegerField(verbose_name='Inteligência', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    power = models.IntegerField(verbose_name='Poder', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    education = models.IntegerField(verbose_name='Educação', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    luck = models.IntegerField(verbose_name='Sorte', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    move_rate = models.IntegerField(verbose_name='Movimento', blank=True, null=False)
    hp = models.IntegerField(verbose_name='HP', blank=True, null=False)
    mp = models.IntegerField(verbose_name='MP', blank=True, null=False)
    san = models.IntegerField(verbose_name='Sanidade', blank=True, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    start_san = models.IntegerField(verbose_name='Sanidade Inicial', blank=True, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_hp = models.IntegerField(verbose_name='HP Máximo', blank=True, null=False)
    max_san = models.IntegerField(verbose_name='Sanidade Máxima', blank=True, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)], default=99)
    max_mp = models.IntegerField(verbose_name='MP Máximo', blank=True, null=False)
    build = models.IntegerField(verbose_name='Corpo', blank=True, null=False)
    bonus_dmg = models.IntegerField(verbose_name='Bonus de dano', blank=True, null=False)
    dodge = models.IntegerField(verbose_name='Esquiva', blank=True, null=False)

    def __str__(self):
        return '{0} ({1})'.format(self.nome_personagem, self.jogador)

    def get_absolute_url(self):
        return '#'#reverse('ficha', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self._state.adding:
           self.max_hp = (self.constitution + self.size) / 10
           self.hp = self.max_hp
           self.max_mp = self.power / 5
           self.mp = self.max_mp
           self.start_san = self.power
           self.san = self.power
           if self.strength < self.size and self.dexterity < self.size:
               self.move_rate = 7
           elif self.strength > self.size and self.dexterity > self.size:
               self.move_rate = 9
           elif self.strength >= self.size or self.dexterity >= self.size:
               self.move_rate = 8
            
           if self.age >= 40:
                self.move_rate = self.move_rate - 1

           str_siz = self.strength + self.size
           if str_siz > 64 and str_siz < 85:
               self.build = -1
               self.bonus_dmg = -1
           elif str_siz > 84 and str_siz < 125:
               self.build = 0
               self.bonus_dmg = 0
           elif str_siz > 124 and str_siz < 165:
               self.build = 1
               self.bonus_dmg = 1

           self.dodge = self.dexterity / 2
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'ficha'
        verbose_name_plural = 'fichas'

class Skills(AbstractBaseModel):

    class Meta:
        verbose_name = 'perícia'
        verbose_name_plural = 'perícias'

class Weapons(AbstractBaseModel):

    class Meta:
        verbose_name = 'arma'
        verbose_name_plural = 'armas'