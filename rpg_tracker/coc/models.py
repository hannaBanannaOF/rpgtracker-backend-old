from os import name
from django.db import models
from django.db.models.enums import IntegerChoices
from rpg_tracker.core.models import FichaBase, AbstractBaseModel, MesaBase
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Skills(AbstractBaseModel):
    class SkillKindChoices(IntegerChoices):
        INTERPERSOAL = 0, "Interpessoal"
        INVESTIGATION = 1, "Investigação"
        COMBAT = 2, "Combate"
        COMMON = 3, "Comum"

    class SkillRarity(IntegerChoices):
        COMMON = 0, 'Comum'
        ANTIQUE = 1, '1920 Era'
        MODERN = 2, 'Moderna'

    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    base_value = models.IntegerField(verbose_name='Valor base', blank=True, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    skill_rarity = models.IntegerField(verbose_name='Raridade', choices=SkillRarity.choices, blank=False, null=False)
    parent_skill = models.ForeignKey(to='self', verbose_name='Skill pai', null=True, blank=True, related_name='specializations', on_delete=models.CASCADE)
    skill_kind = models.IntegerField(verbose_name='Tipo de skill', choices=SkillKindChoices.choices, blank=False, null=False)

    @property
    def full_name(self):
        if self.parent_skill is not None:
            return '{0} ({1})'.format(self.name, self.parent_skill.name)
        return self.name

    @property
    def absolute_value(self):
        return self.parent_skill.base_value if self.parent_skill is not None and (self.base_value is None or self.base_value == 0) else self.base_value

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'perícia'
        verbose_name_plural = 'perícias'

class Ocupation(AbstractBaseModel):
    class SkillPointsCalcRuleChoices(IntegerChoices):
        EDU4 = 0, "EDU x 4"
        EDU2INT2 = 1, "EDU x 2 + INT x 2"
        EDU2APP2 = 2, "EDU x 2 + APP x 2"
        EDU2STR2 = 3, "EDU x 2 + STR x 2"
        EDU2DEX2 = 4, "EDU x 2 + DEX x 2"
        EDU2STRORDEX2 = 5, "EDU x 2 + (STR x 2 ou DEX x 2)"
        EDU2APPORDEX2 = 6, "EDU x 2 + (APP x 2 ou DEX x 2)"
        EDU2STRORAPPORDEX2 = 7, "EDU x 2 + (STR x 2 ou DEX x 2 ou APP x 2)"
    
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    description = models.TextField(verbose_name='Descrição', blank=True, null=False)
    skill_points_calc_rule = models.IntegerField(verbose_name='Regra de cálculo para Pontos de Ocupação', choices=SkillPointsCalcRuleChoices.choices, default=0)
    credit_rating_min = models.IntegerField(verbose_name='Rank de Crédito Mínimo', null=False, blank=False)
    credit_rating_max = models.IntegerField(verbose_name='Rank de Crédito Máximo', null=False, blank=False)
    sugested_contacts = models.TextField(verbose_name='Contatos sugeridos', blank=True, null=True)
    skills = models.ManyToManyField(to=Skills, related_name='ocupations', verbose_name='Perícias disponiveis', blank=True)
    skill_choices = models.IntegerField(verbose_name='Qtde de skills como especialidades pessoais ou de época', blank=True, null=True)
    skill_choices_2 = models.IntegerField(verbose_name='Qtde de skills do tipo', null=True, blank=True)
    skill_choice_2_kind = models.IntegerField(verbose_name='Tipo da skill', choices=Skills.SkillKindChoices.choices, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ocupação'
        verbose_name_plural = 'ocupações'

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
    dodge_improv = models.BooleanField(verbose_name='Improv. Check na esquiva', null=False, default=False, blank=False)
    language_own = models.IntegerField(verbose_name='Idioma natural', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    language_own_improv = models.BooleanField(verbose_name='Improv. Check no idioma natural', null=False, default=False, blank=False)
    ocupation = models.ForeignKey(to=Ocupation, on_delete=models.RESTRICT, verbose_name='Ocupação', related_name='fichas')
    ocupational_skill_points = models.IntegerField(verbose_name='Pontos de perícia ocupacionais', blank=True, null=False)
    personal_interest_skill_points = models.IntegerField(verbose_name='Pontos de perícia de interese pessoais', blank=True, null=False)
    major_wound = models.BooleanField(verbose_name='Major wound', blank=False, null=False, default=False)
    temporary_insanity = models.BooleanField(verbose_name='Insanidade Temporária', blank=False, null=False, default=False)
    indefinity_insanity = models.BooleanField(verbose_name='Insanidade Indefinida', blank=False, null=False, default=False)
    credit_rating = models.IntegerField(verbose_name='Renk de crédito', blank=True, null=True)
    cthulhu_mythos = models.IntegerField(verbose_name='Cthulhu Mythos', blank=True, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.nome_personagem, self.jogador)

    def get_absolute_url(self):
        return reverse('coc:ficha', kwargs={'pk': self.pk})

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
            self.language_own = self.education
            
            if self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU4:
                self.ocupational_skill_points = self.education * 4
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2APP2:
                self.ocupational_skill_points = self.education * 2 + self.appearence * 2
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2DEX2:
                self.ocupational_skill_points = self.education * 2 + self.dexterity * 2
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2INT2:
                self.ocupational_skill_points = self.education * 2 + self.inteligence * 2 
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2STR2:
                self.ocupational_skill_points = self.education * 2 + self.strength * 2 
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2APPORDEX2:
                if self.appearence >= self.dexterity:
                    self.ocupational_skill_points = self.education * 2 + self.appearence * 2
                else:
                    self.ocupational_skill_points = self.education * 2 + self.dexterity * 2
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2STRORDEX2:
                if self.strength >= self.dexterity:
                    self.ocupational_skill_points = self.education * 2 + self.strength * 2
                else:
                    self.ocupational_skill_points = self.education * 2 + self.dexterity * 2
            elif self.ocupation.skill_points_calc_rule == Ocupation.SkillPointsCalcRuleChoices.EDU2STRORAPPORDEX2:
                if self.strength >= self.appearence and self.strength >= self.dexterity:
                    self.ocupational_skill_points = self.education * 2 + self.strength * 2
                elif self.appearence >= self.strength and self.appearence >= self.dexterity:
                    self.ocupational_skill_points = self.education * 2 + self.appearence * 2
                else:
                    self.ocupational_skill_points = self.education * 2 + self.dexterity * 2

        self.personal_interest_skill_points = self.inteligence * 2

        super().save(*args, **kwargs)

    def get_skill_list(self):
        skill_list = {}
        for s in Skills.objects.all():
            skill_list.update({str(s.pk) : {"name":s.full_name,"value": s.absolute_value,"improv":False}})
        
        for s in self.skills.all():
            if skill_list.get(str(s.skill.pk)) is not None:
                skill_list.update({str(s.skill.pk) : {"name":s.skill.full_name,"value":s.value,"improv":s.skill_improv}})

        skill_list.update({"credit-ratind":{"name":"Credit rating", "value":self.credit_rating if self.credit_rating is not None else 0, "improv":False}})
        skill_list.update({"dodge":{"name":"Dodge", "value":self.dodge, "improv":self.dodge_improv}})
        skill_list.update({"cthulhu-mythos":{"name":"Cthulhu Mythos", "value":self.cthulhu_mythos if self.cthulhu_mythos is not None else 0, "improv":False}})
        skill_list.update({"language-own":{"name":"Own (Language)", "value":self.language_own, "improv":self.language_own_improv}})

        return dict(sorted(skill_list.items(), key=lambda k_v: k_v[1]["name"]))

    class Meta:
        verbose_name = 'ficha'
        verbose_name_plural = 'fichas'

class SkillsOnFicha(AbstractBaseModel):
    ficha = models.ForeignKey(to=FichaCOC, related_name='skills', blank=False, null=False, verbose_name='Ficha', on_delete=models.RESTRICT)
    skill = models.ForeignKey(to=Skills, blank=False, null=False, related_name='fichas', verbose_name='Skill', on_delete=models.RESTRICT)
    value = models.IntegerField(verbose_name='Valor', blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    skill_improv = models.BooleanField(verbose_name='Improvement', default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.skill, self.ficha)

    class Meta:
        verbose_name = 'perícia em ficha'
        verbose_name_plural = 'perícias em fichas'

class Ammo(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    rounds_shot_with_each = models.IntegerField(verbose_name='Tiros com cada munição', blank=False, null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'munição'
        verbose_name_plural = 'munições'

class Weapons(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=50)
    ammo = models.ForeignKey(to=Ammo, related_name='guns', blank=True, null=True, verbose_name='Munição', on_delete=models.RESTRICT)
    range = models.IntegerField(verbose_name='Alcance', null=True, blank=True)
    attacks = models.IntegerField(verbose_name='Ataques por round', null=False, blank=False)
    malfunction = models.IntegerField(verbose_name='Falha', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_melee = models.BooleanField(verbose_name='Mano a mano', blank=False, null=False, default=True)
    damage = models.CharField(verbose_name='Dano', blank=False, null=False, max_length=20)
    skill_used = models.ForeignKey(to=Skills, verbose_name='Skill usada', blank=False, null=False, related_name='weapons', on_delete=models.RESTRICT)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'arma'
        verbose_name_plural = 'armas'

class WeaponsInFicha(AbstractBaseModel):
    weapon = models.ForeignKey(to=Weapons, on_delete=models.RESTRICT, related_name='fichas', blank=False, null=False, verbose_name='Arma')
    ficha = models.ForeignKey(to=FichaCOC, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Ficha', related_name='weapons')
    ammo_left = models.IntegerField(verbose_name='Munição disponível', blank=True, null=True)
    rounds_left = models.IntegerField(verbose_name='Tiros restantes', null=True, blank=True)
    nickname = models.CharField(verbose_name='Apelido', max_length=50, null=True, blank=True)

    @property
    def total_ammo_left(self):
        return (self.ammo_left if self.ammo_left is not None else 0) * self.weapon.ammo.rounds_shot_with_each if not self.weapon.is_melee else None

    def __str__(self):
        return '{0} - {1}'.format(self.weapon, self.ficha)

    @property
    def normal_success_value(self):
        has_skill = None
        for skill in self.ficha.skills.all():
            if self.weapon.skill_used.pk == skill.skill.pk:
                has_skill = skill
                break
        return has_skill.value if has_skill is not None else self.weapon.skill_used.base_value

    @property
    def get_ficha_description(self):
        return self.nickname if self.nickname is not None and self.nickname != '' else self.weapon.name

    class Meta:
        verbose_name = 'arma em ficha'
        verbose_name_plural = 'armas em fichas'

class MesaCOC(MesaBase):
    class Meta:
        verbose_name = 'mesa'
        verbose_name_plural = 'mesas'