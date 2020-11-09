from django.db import models
from rpg_tracker.core.models import FichaBase, AbstractBaseModel
from django.urls import reverse

# Create your models here.
class RaceTraitsDND(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=50)
    description = models.TextField(verbose_name='Descrição', null=False, blank=False)

    def __str__(self):
        return self.name

    @property
    def name_trim(self):
        return self.name.replace(' ', '_').lower()

    class Meta:
        verbose_name = 'traço racial'
        verbose_name_plural = 'traços raciais'

class LanguagesDND(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'idioma'        
        verbose_name_plural = 'idiomas'

class RacesDND(AbstractBaseModel):
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
    traits = models.ManyToManyField(RaceTraitsDND, 'tracos', verbose_name='Traços')
    languages = models.ManyToManyField(LanguagesDND, 'idiomas', verbose_name='Idiomas')


    def __str__(self):
        ret = ''
        if self.homebrew:
            ret = ' (Homebrew)'
        return '{0}{1}'.format(self.race_name, ret)

    class Meta:
        verbose_name = 'raça'
        verbose_name_plural = 'raças'

class ClasseDND(AbstractBaseModel):
    nome = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    descricao = models.TextField(verbose_name='Descrição', blank=False, null=False)
    saving_str = models.BooleanField(verbose_name='Proficiência em resistência de força', blank=False, null=False, default=False)
    saving_dex = models.BooleanField(verbose_name='Proficiência em resistência de destreza', blank=False, null=False, default=False)
    saving_con = models.BooleanField(verbose_name='Proficiência em resistência de constituição', blank=False, null=False, default=False)
    saving_int = models.BooleanField(verbose_name='Proficiência em resistência de inteligência', blank=False, null=False, default=False)
    saving_wis = models.BooleanField(verbose_name='Proficiência em resistência de sabedoria', blank=False, null=False, default=False)
    saving_cha = models.BooleanField(verbose_name='Proficiência em resistência de carisma', blank=False, null=False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'classe'
        verbose_name_plural = 'classes'

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

    def calc_mod(self, mod, has_proficiency=False):
        if has_proficiency:
            bonus = self.proficiency_bonus
        else:
            bonus = 0
        result = ((mod-10)//2)+bonus
        if result >= 0:
            ret = '+'
        else:
            ret = ''
        return ret+str(result)

    def get_absolute_url(self):
        return reverse('dnd:ficha_detalhe', args=[str(self.pk)])

    def to_dict(self):
        return {
            'nome' : self.nome_personagem,
            'raca' : {
                'nome' : self.race.race_name,
                'idiomas' : self.race.languages
            },
            'jogador' : self.jogador,
            'xp' : self.xp,
            'alinhamento' : self.AlignmentKind.choices[self.alignment][1],
            'str' : {
                'value' : self.strenght + self.race.str_inc,
                'mod' : self.calc_mod(self.strenght + self.race.str_inc),
                'saving' : self.classes.filter(classe__saving_str=True).count() > 0,
                'saving_value' : self.calc_mod(self.strenght + self.race.str_inc, self.classes.filter(classe__saving_str=True).count() > 0)
            },
            'dex' : {
                'value' : self.dexterity + self.race.dex_inc,
                'mod' : self.calc_mod(self.dexterity + self.race.dex_inc),
                'saving' : self.classes.filter(classe__saving_dex=True).count() > 0,
                'saving_value' : self.calc_mod(self.dexterity + self.race.dex_inc, self.classes.filter(classe__saving_dex=True).count() > 0)
            },
            'con' : {
                'value' : self.constitution + self.race.con_inc,
                'mod' : self.calc_mod(self.constitution + self.race.con_inc),
                'saving' : self.classes.filter(classe__saving_con=True).count() > 0,
                'saving_value' : self.calc_mod(self.constitution + self.race.con_inc, self.classes.filter(classe__saving_con=True).count() > 0)
            },
            'int' : {
                'value' : self.inteligence + self.race.int_inc,
                'mod' : self.calc_mod(self.inteligence + self.race.int_inc),
                'saving' : self.classes.filter(classe__saving_int=True).count() > 0,
                'saving_value' : self.calc_mod(self.inteligence + self.race.int_inc, self.classes.filter(classe__saving_int=True).count() > 0)
            },
            'wis' : {
                'value' : self.wisdom + self.race.wis_inc,
                'mod' : self.calc_mod(self.wisdom + self.race.wis_inc),
                'saving' : self.classes.filter(classe__saving_wis=True).count() > 0,
                'saving_value' : self.calc_mod(self.wisdom + self.race.wis_inc, self.classes.filter(classe__saving_wis=True).count() > 0)
            },
            'cha' : {
                'value' : self.charisma + self.race.cha_inc,
                'mod' : self.calc_mod(self.charisma + self.race.cha_inc),
                'saving' : self.classes.filter(classe__saving_cha=True).count() > 0,
                'saving_value' : self.calc_mod(self.charisma + self.race.cha_inc, self.classes.filter(classe__saving_cha=True).count() > 0)
            },
            'skills' : [
                {
                    'ident' : 'acrobacia',  
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc),
                    'text' : 'Acrobacia',
                    'use' : 'Des'  
                },
                {
                    'ident' : 'adestrar',
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc),
                    'text' : 'Adestrar animais',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'arcanismo',
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc),
                    'text' : 'Arcanismo',
                    'use' : 'Int'
                },
                {
                    'ident' : 'atletismo',
                    'value' : self.calc_mod(self.strenght+self.race.str_inc),
                    'text' : 'Atletismo',
                    'use' : 'For'
                },
                {
                    'ident' : 'atuacao',
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc),
                    'text' : 'Atuação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'enganacao',
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc),
                    'text' : 'Enganação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'furtividade',
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc),
                    'text' : 'Furtividade',
                    'use' : 'Dex'
                },
                {
                    'ident' : 'historia',
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc),
                    'text' : 'História',
                    'use' : 'Int'
                },
                {
                    'ident' : 'intimnidacao',
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc),
                    'text' : 'Intimidação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'intuicao',
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc),
                    'text' : 'Intuição',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'investigacao',
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc),
                    'text' : 'Investigação',
                    'use' : 'Int'
                },
                {
                    'ident' : 'medicina',
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc),
                    'text' : 'Medicina',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'natureza',
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc),
                    'text' : 'Natureza',
                    'use' : 'Int'
                },
                {
                    'ident' : 'percepcao',
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc),
                    'text' : 'Percepção',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'persuasao',
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc),
                    'text' : 'Persuasão',
                    'use' : 'Car'
                },
                {
                    'ident' : 'prestidigitacao',
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc),
                    'text' : 'Prestidigitação',
                    'use' : 'Des'
                },
                {
                    'ident' : 'religiao',
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc),
                    'text' : 'Religião',
                    'use' : 'Int'
                },
                {
                    'ident' : 'sobrevivencia',
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc),
                    'text' : 'Sobrevivência',
                    'use' : 'Sab'
                }
            ],
            'tracos' : self.race.traits,
            'classes' : self.classes
        }

    class Meta:
        verbose_name='ficha'
        verbose_name_plural='fichas'

class ClassesFichaDND(AbstractBaseModel):
    classe = models.ForeignKey(ClasseDND, on_delete=models.CASCADE, related_name='fichas')
    ficha = models.ForeignKey(FichaDND, on_delete=models.CASCADE, related_name='classes')
    level = models.IntegerField(verbose_name='Nível da classe', null=False, blank=False, default=1)

    def __str__(self):
        return '{0}(LVL {2}) em {1}'.format(self.classe, self.ficha, self.level)

    class Meta:
        verbose_name = 'classe em ficha'
        verbose_name_plural = 'classes em fichas'