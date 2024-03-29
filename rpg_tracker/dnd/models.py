from django.db import models
from django.db.models.enums import Choices, IntegerChoices
from rpg_tracker.core.models import FichaBase, AbstractBaseModel
from django.urls import reverse
from multiselectfield import MultiSelectField
# Create your models here.
SkillChoices = (
    (0, 'Acrobacia'),
    (1, 'Adestrar animais'),
    (2, 'Arcanismo'),
    (3, 'Atletismo'),
    (4, 'Atuação'),
    (5, 'Enganação'),
    (6, 'Furtividade'),
    (7, 'História'),
    (8, 'Intimidação'),
    (9, 'Intuição'),
    (10, 'Investigação'),
    (11, 'Medicina'),
    (12, 'Natureza'),
    (13, 'Percepção'),
    (14, 'Persuasão'),
    (15, 'Prestidigitação'),
    (16, 'Religião'),
    (17, 'Sobrevivência'))

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
    skills = MultiSelectField(choices=SkillChoices, verbose_name='Proficiência em perícias', null=True, blank=True)
    skill_choice_limit = models.IntegerField(verbose_name='Limite de escolha de perícias na ficha', blank=True, null=True, help_text='se 0 ou vazio, não existe limite, pega todas as perícias selecionadas')
    
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
    prequesite_races = models.ManyToManyField(RacesDND, 'racas_prereq', verbose_name='Prerequisitos de raça', blank=True)
    skills = MultiSelectField(choices=SkillChoices, verbose_name='Proficiência em perícias', null=True, blank=True)
    skill_choice_limit = models.IntegerField(verbose_name='Limite de escolha de perícias na ficha', blank=True, null=True, help_text='se 0 ou vazio, não existe limite, pega todas as perícias selecionadas')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'classe'
        verbose_name_plural = 'classes'

class AntecedentesDND(AbstractBaseModel):
    pass

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
    race = models.ForeignKey(RacesDND, on_delete=models.CASCADE, related_name='raca', verbose_name='Raça')
    race_skill_selected = MultiSelectField(choices=SkillChoices, verbose_name='Proficiência em perícias da raça', null=True, blank=True)

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

    def check_skill_prof(self, proficiency):
        new_skillset = []
        # classes proficiency
        for c in self.classes.all():
            if repr(c.selected_skills) != "[]":
                new_skillset.extend(repr(c.selected_skills).replace("'", "").replace(" ","").strip("[").strip("]").split(','))

        # race proficiency
        if repr(self.race_skill_selected) != "[]":
            new_skillset.extend(repr(self.race_skill_selected).replace("'", "").replace(" ","").strip("[").strip("]").split(','))
        
        # background proficiency
        #todo
        
        return proficiency in [int(v) for v in new_skillset]

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
                    'has_skill' : self.check_skill_prof(0),
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc, self.check_skill_prof(0)),
                    'text' : 'Acrobacia',
                    'use' : 'Des'  
                },
                {
                    'ident' : 'adestrar',
                    'has_skill' : self.check_skill_prof(1),
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc, self.check_skill_prof(1)),
                    'text' : 'Adestrar animais',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'arcanismo',
                    'has_skill' : self.check_skill_prof(2),
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc, self.check_skill_prof(2)),
                    'text' : 'Arcanismo',
                    'use' : 'Int'
                },
                {
                    'ident' : 'atletismo',
                    'has_skill' : self.check_skill_prof(3),
                    'value' : self.calc_mod(self.strenght+self.race.str_inc, self.check_skill_prof(3)),
                    'text' : 'Atletismo',
                    'use' : 'For'
                },
                {
                    'ident' : 'atuacao',
                    'has_skill' : self.check_skill_prof(4),
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc, self.check_skill_prof(4)),
                    'text' : 'Atuação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'enganacao',
                    'has_skill' : self.check_skill_prof(5),
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc, self.check_skill_prof(5)),
                    'text' : 'Enganação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'furtividade',
                    'has_skill' : self.check_skill_prof(6),
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc, self.check_skill_prof(6)),
                    'text' : 'Furtividade',
                    'use' : 'Dex'
                },
                {
                    'ident' : 'historia',
                    'has_skill' : self.check_skill_prof(7),
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc, self.check_skill_prof(7)),
                    'text' : 'História',
                    'use' : 'Int'
                },
                {
                    'ident' : 'intimnidacao',
                    'has_skill' : self.check_skill_prof(8),
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc, self.check_skill_prof(8)),
                    'text' : 'Intimidação',
                    'use' : 'Car'
                },
                {
                    'ident' : 'intuicao',
                    'has_skill' : self.check_skill_prof(9),
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc, self.check_skill_prof(9)),
                    'text' : 'Intuição',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'investigacao',
                    'has_skill' : self.check_skill_prof(10),
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc, self.check_skill_prof(10)),
                    'text' : 'Investigação',
                    'use' : 'Int'
                },
                {
                    'ident' : 'medicina',
                    'has_skill' : self.check_skill_prof(11),
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc, self.check_skill_prof(11)),
                    'text' : 'Medicina',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'natureza',
                    'has_skill' : self.check_skill_prof(12),
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc, self.check_skill_prof(12)),
                    'text' : 'Natureza',
                    'use' : 'Int'
                },
                {
                    'ident' : 'percepcao',
                    'has_skill' : self.check_skill_prof(13),
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc, self.check_skill_prof(13)),
                    'text' : 'Percepção',
                    'use' : 'Sab'
                },
                {
                    'ident' : 'persuasao',
                    'has_skill' : self.check_skill_prof(14),
                    'value' : self.calc_mod(self.charisma+self.race.cha_inc, self.check_skill_prof(14)),
                    'text' : 'Persuasão',
                    'use' : 'Car'
                },
                {
                    'ident' : 'prestidigitacao',
                    'has_skill' : self.check_skill_prof(15),
                    'value' : self.calc_mod(self.dexterity+self.race.dex_inc, self.check_skill_prof(15)),
                    'text' : 'Prestidigitação',
                    'use' : 'Des'
                },
                {
                    'ident' : 'religiao',
                    'has_skill' : self.check_skill_prof(16),
                    'value' : self.calc_mod(self.inteligence+self.race.int_inc, self.check_skill_prof(16)),
                    'text' : 'Religião',
                    'use' : 'Int'
                },
                {
                    'ident' : 'sobrevivencia',
                    'has_skill' : self.check_skill_prof(17),
                    'value' : self.calc_mod(self.wisdom+self.race.wis_inc , self.check_skill_prof(17)),
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
    selected_skills = MultiSelectField(choices=SkillChoices, verbose_name='Proficiência em perícias selecionadas', null=True, blank=True)

    def __str__(self):
        return '{0}(LVL {2}) em {1}'.format(self.classe, self.ficha, self.level)

    class Meta:
        verbose_name = 'classe em ficha'
        verbose_name_plural = 'classes em fichas'


class TrapsDND(AbstractBaseModel):
    class DangerKind(IntegerChoices):
        SETBACK = 0, 'Setback'
        MODERATE = 1, 'Moderado'
        DANGEROUS = 2, 'Perigoso'
        PERICULOUS = 3, 'Muito perigoso'
        DEADLY = 4, 'Mortal'
    
    class LevelKind(IntegerChoices):
        LVL_1_4 = 0, '1-4'
        LVL_5_8 = 1, '5-8'
        LVL_9_12 = 2, '9-12'
        LVL_13_16 = 3, '13-16'
        LVL_17_20 = 4, '17-20'

    name = models.CharField('Nome', max_length=200, null=False, blank=False)
    kind = models.CharField('Tipo', max_length=200, null=False, blank=False)
    level = models.IntegerField('Nível', choices=LevelKind.choices, null=False, blank=False)
    danger = models.IntegerField('Nível de perigo', choices=DangerKind.choices, null=False, blank=False)
    description = models.TextField('Descrição', null=False, blank=False)
    trigger_kind = models.CharField('Tipo de gatilho', max_length=200, null=False, blank=False)
    trigger_description = models.TextField('Descrição do gatilho', null=False, blank=False)
    effect_kind = models.CharField('Tipo de efeito', max_length=200, null=False, blank=False)
    effect_description = models.TextField('Descrição do efeito', null=False, blank=False)
    countermeasures = models.TextField('Contramedidas', null=False, blank=False)

    def __str__(self):
        return '{0}(LVL {1}, {2})'.format(self.name, self.LevelKind.choices[self.level][1], self.DangerKind.choices[self.danger][1])

    def to_dict(self):
        return {
            'name':self.name,
            'kind':self.kind,
            'level':self.LevelKind.choices[self.level][1],
            'danger': self.DangerKind.choices[self.danger][1],
            'description': self.description,
            'trigger': {
                'kind':self.trigger_kind,
                'description':self.trigger_description
            },
            'effect': {
                'kind':self.effect_kind,
                'description':self.effect_description
            },
            'countermeasures':self.countermeasures
        }

    class Meta:
        verbose_name = 'armadilha'
        verbose_name_plural = 'armadilhas'