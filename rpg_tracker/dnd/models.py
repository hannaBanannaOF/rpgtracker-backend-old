from django.db import models
from rpg_tracker.core.models import FichaBase

# Create your models here.
class RacesDND(models.Model):
    race_name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    race_desc = models.TextField(verbose_name='Descrição', blank=True, null=True)
    str_inc = models.IntegerField(verbose_name='Incremento de força', blank=False, null=False, default=0)
    dex_inc = models.IntegerField(verbose_name='Incremento de destreza', blank=False, null=False, default=0)
    con_inc = models.IntegerField(verbose_name='Incremento de constituição', blank=False, null=False, default=0)
    int_inc = models.IntegerField(verbose_name='Incremento de inteligência', blank=False, null=False, default=0)
    wis_inc = models.IntegerField(verbose_name='Incremento de sabedoria', blank=False, null=False, default=0)
    cha_inc = models.IntegerField(verbose_name='Incremento de carisma', blank=False, null=False, default=0)
    mov_speed = models.FloatField(verbose_name='Deslocamento', blank=False, null=False, default=0)
    homebrew = models.BooleanField(verbose_name='Homebrew', blank=False, null=False, default=True)

    def __str__(self):
        ret = ''
        if self.homebrew:
            ret = ' (Homebrew)'
        return '{0}{1}'.format(self.race_name, ret)

    class Meta:
        verbose_name = 'raça'
        verbose_name_plural = 'raças'

class FichaDND(FichaBase):
    class AlignmentKind(models.IntegerChoices):
        LAWFUL_GOOD = 0, 'Leal e bom'
        LAWFUL_NEUTRAL = 1, 'Leal e neutro'
        LAWFUL_EVIL = 2, 'Leal e mau'
        NEUTRAL_GOOD = 3, 'Neutro e bom'
        TRUE_NEUTRAL = 4, 'Neutro e neutro'
        NEUTRAL_EVIL = 5, 'Neutro e mau'
        CHAOTIC_GOOD = 6, 'Caótico e bom' 
        CHAOTIC_NEUTRAL = 7, 'Caótico e neutro' 
        CHAOTIC_EVIL = 8, 'Caótico e mau'

    xp = models.IntegerField(verbose_name='XP', blank=False, null=False, default=0)
    alignment = models.IntegerField(verbose_name='Alinhamento', blank=False, null=False, choices=AlignmentKind.choices)
    strenght = models.IntegerField(verbose_name='Força', blank=False, null=False)
    dexterity = models.IntegerField(verbose_name='Destreza', blank=False, null=False)
    constitution = models.IntegerField(verbose_name='Constituição', blank=False, null=False)
    inteligence = models.IntegerField(verbose_name='Inteligência', blank=False, null=False)
    wisdom = models.IntegerField(verbose_name='Sabedoria', blank=False, null=False)
    charisma = models.IntegerField(verbose_name='Carisma', blank=False, null=False)
    character_level = models.IntegerField(verbose_name='Nível de personagem', blank=False, null=False, default=1)
    proficiency_bonus = models.IntegerField(verbose_name='Bônus de proficiência', null=False, blank=False, default=2)
    race = models.ForeignKey(RacesDND, on_delete=models.CASCADE, related_name='raca')

    def __str__(self):
        return '{0} ({1})'.format(self.nome_personagem, self.jogador)

    def calc_mod(self, mod):
        if mod > 9:
            ret = '+'
        else:
            ret = ''
        return ret+str((mod-10)//2)

    def to_dict(self):
        return {
            'nome' : self.nome_personagem,
            'raca' : {
                'nome' : self.race.race_name
            },
            'str' : {
                'value' : self.strenght + self.race.str_inc,
                'mod' : self.calc_mod(self.strenght + self.race.str_inc)
            },
            'dex' : {
                'value' : self.dexterity + self.race.dex_inc,
                'mod' : self.calc_mod(self.dexterity + self.race.dex_inc)
            },
            'con' : {
                'value' : self.constitution + self.race.con_inc,
                'mod' : self.calc_mod(self.constitution + self.race.con_inc)
            },
            'int' : {
                'value' : self.inteligence + self.race.int_inc,
                'mod' : self.calc_mod(self.inteligence + self.race.int_inc)
            },
            'wis' : {
                'value' : self.wisdom + self.race.wis_inc,
                'mod' : self.calc_mod(self.wisdom + self.race.wis_inc)
            },
            'cha' : {
                'value' : self.charisma + self.race.cha_inc,
                'mod' : self.calc_mod(self.charisma + self.race.cha_inc)
            }
        }

    class Meta:
        verbose_name='ficha'
        verbose_name_plural='fichas'