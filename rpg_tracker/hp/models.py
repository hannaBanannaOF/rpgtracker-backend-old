from django.core import validators
from django.db.models.enums import IntegerChoices
from django.db.models.fields import IntegerField, NullBooleanField
from django.utils import translation
from rpg_tracker.core.models import AbstractBaseModel, FichaBase, MesaBase
from django.db import models
from django.urls import reverse

# Create your models here.
class Equipamentos(AbstractBaseModel):
    nome = models.CharField(verbose_name="Nome", null=False, blank=False, max_length=255)
    material_escolar = models.BooleanField(verbose_name="É material escolar", null=False, blank=False, default=False)

class Varinha(AbstractBaseModel):
    class Nucleos(IntegerChoices):
        FENIX = 0, "Pena da cauda de fênix"
        DRAGAO = 1, "Corda de coração de dragão"
        UNICORNIO = 2, "Pelo de unicórnio"
        VEELA = 3, "Cabelo de veela"
        SERPENTE_CHIFRUDA = 4, "Chifre de serpente chifruda dos rios"

    class Madeiras(IntegerChoices):
        BETULA = 0, "Bétula"
        SOVIEIRA = 1, "Sovieira"
        FREIXO = 2, "Freixo"
        AMIEIRO = 3, "Amieiro"
        SABUGUEIRO = 4, "Sabugueiro"
        ABRUNHEIRO =  5, "Abrunheiro"
        CARVALHO = 6, "Carvalho"
        AZEVINHO = 7, "Azevinho"
        AVELA = 8, "Avelã"
        VIDEIRA = 9, "Videira"
        HEDERA = 10, "Hedera"
        SEQUOIA = 11, "Sequoia"

    class Flexibilidade(IntegerChoices):
        DOBRAVEL = 0, "Dobrável"
        SURP_SUAVE = 1, "Surpreendentemente suave"
        SUAVE = 2, "Suave"
        LIG_SUAVE = 3, "Ligeiramente suave"
        BAST_CURVADA = 4, "Bastante curvada"
        MUITO_FLEX = 5, "Muito flexível"
        BAST_FLEX = 6, "Bastante flexível"
        FLEX = 7, "Flexível"
        RAZ_FLEX = 8, "Razoavelmente flexível"
        MALEA = 9, "Maleável"
        FRAGIL = 10, "Frágil"
        ASPERA = 11, "Áspera"
        MACICA = 12, "Maciça"
        VISCOSA = 13, "Viscosa"
        RIGIDA = 14, "Rígida"
        INFLEX = 15, "Inflexível"
        LEV_INFLEX = 16, "Levemente inflexível"
        RESOLUT = 17, "Resoluta"
        MACIA = 18, "Macia"

    nucleo = models.IntegerField(verbose_name="Núcleo", null=False, blank=False, choices=Nucleos.choices)
    madeira = models.IntegerField(verbose_name="Madeira", null=False, blank=False, choices=Madeiras.choices)
    tamanho = models.FloatField(verbose_name="Tamanho", null=False, blank=False)
    flexibilidade = models.IntegerField(verbose_name="Flexibilidade", null=False, blank=False, choices=Flexibilidade.choices)

    class Meta:
        verbose_name = 'varinha'
        verbose_name_plural = 'varinhas'

class FichaHP(FichaBase):
    class CasaHogwarts(IntegerChoices):
        GRIFFINDOR = 0, "Grifinória"
        SLYTHERIN = 1, "Sonserina"
        RAVENCLAW = 2, "Corvinal"
        HUFFLEPUFF = 3, "Lufa-lufa"

    escola = models.CharField(verbose_name="Escola", null=True, blank=True, max_length=255)
    ano_escolar = models.IntegerField(verbose_name="Ano Escolar", null=False, blank=False, default=1, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(7)])
    casa_hogwarts = models.IntegerField(verbose_name="Casa de Hogwarts", null=True, blank=True, choices=CasaHogwarts.choices)
    familiar = models.CharField(verbose_name="Familiar (nome & tipo)", null=True, blank=True, max_length=255)
    atletismo = models.IntegerField(verbose_name="Atletismo", null=False, blank=False, default=0)
    conhecimento = models.IntegerField(verbose_name="Conhecimento", null=False, blank=False, default=0)
    intriga = models.IntegerField(verbose_name="Intriga", null=False, blank=False, default=0)
    magia = models.IntegerField(verbose_name="Magia", null=False, blank=False, default=0)
    varinha = models.ForeignKey(to=Varinha, verbose_name="Varinha", related_name="bruxo", null=True, blank=True, on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        self.magia = self.ano_escolar
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "{0} - {1}".format(self.nome_personagem, self.jogador)

    def get_absolute_url(self):
        return reverse('hp:ficha', kwargs={'pk': self.pk})

    def get_children(self, skill):
        ret = []
        for x in skill.especializacoes.all():
            per = self.pericias.filter(pericia_id=x.id).filter(ficha__id=self.id).first()
            ret.append({
                'nome' : x.nome,
                'valor' : per.valor if per is not None else 0,
                'children' : self.get_children(x.pericia),
                'hint' : ''
            })
        for x in EspecializacoesCustomizadasPlayer.objects.filter(pericia_pai=skill).filter(ficha__id=self.id).all():
            ret.append({
                'nome' : x.nome,
                'valor' : x.valor,
                'children' : [],
                'hint' : x.hint
            })
        return ret

    def get_parents(self, aptidao):
        ret = []
        for x in PericiasEspecializacoes.objects.filter(aptidao=aptidao).all():
            per = self.pericias.filter(pericia_id=x.id).first()
            ret.append({
                'nome' : x.nome,
                'valor' : per.valor if per is not None else 0,
                'children' : self.get_children(x),
                'hint' : ''
            }) 
        return ret

    def get_pericias_atletismo(self):
        return self.get_parents(0)

    def get_pericias_conhecimento(self):
        return self.get_parents(2)

    def get_pericias_intriga(self):
        return self.get_parents(1)

    def get_pericias_magia(self):
        return self.get_parents(3)

    class Meta:
        verbose_name = 'ficha'
        verbose_name_plural = 'fichas'

class EquipamentoFicha(AbstractBaseModel):
    equip = models.ForeignKey(to=Equipamentos, related_name="fichas", verbose_name="Equipamentos", on_delete=models.RESTRICT, null=False, blank=False)
    ficha = models.ForeignKey(to=FichaHP, related_name="equipamentos", verbose_name="Ficha", on_delete=models.CASCADE, null=False, blank=False)

class PericiasEspecializacoes(AbstractBaseModel):
    class AptidaoChoices(IntegerChoices):
        ATLETISMO = 0, "Atletismo"
        INTRIGA = 1, "Intriga"
        CONHECIMENTO = 2, "Conhecimento"
        MAGIA = 3, "Magia"
    
    nome = models.CharField(verbose_name="Nome", null=False, blank=False, max_length=255)
    aptidao = models.IntegerField(verbose_name="Aptidão", null=True, blank=True, choices=AptidaoChoices.choices)
    pericia_pai = models.ForeignKey(to='self', related_name='especializacoes', blank=True, null=True, verbose_name='Perícia pai', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return "{0}{1}{2}".format(self.nome, " ("+str(self.AptidaoChoices.choices[self.aptidao][1])+")" if self.aptidao is not None else "", " - "+str(self.pericia_pai) if self.pericia_pai is not None else "")

    class Meta:
        verbose_name = 'perícia e aptidão'
        verbose_name_plural = 'perícias e aptidões'

class EspecializacoesCustomizadasPlayer(AbstractBaseModel):
    ficha = models.ForeignKey(to=FichaHP, related_name="especializacoes_custom", blank=False, null=False, verbose_name='Ficha', on_delete=models.RESTRICT)
    nome = models.CharField(verbose_name="Nome", null=False, blank=False, max_length=255)
    pericia_pai = models.ForeignKey(to=PericiasEspecializacoes, related_name='especializacoes_custom', blank=False, null=False, verbose_name='Perícia pai', on_delete=models.RESTRICT)
    valor = models.IntegerField(verbose_name="Valor", null=False, blank=False)
    hint = models.CharField(verbose_name="Dica", null=False, blank=False, max_length=255)

    class Meta:
        verbose_name = 'especialização customizada por player'
        verbose_name_plural = 'especializações customizadas por player'

class PericiasEspecializacoesFicha(AbstractBaseModel):
    ficha = models.ForeignKey(to=FichaHP, related_name="pericias", blank=False, null=False, verbose_name='Ficha', on_delete=models.RESTRICT)
    pericia = models.ForeignKey(to=PericiasEspecializacoes, related_name='fichas', blank=False, null=False, verbose_name='Perícias e especializações', on_delete=models.RESTRICT)
    valor = models.IntegerField(verbose_name="Valor", null=False, blank=False)

    class Meta:
        verbose_name = 'perícia/especialização em ficha'
        verbose_name_plural = 'perícias/especializações em fichas'

class CriaturaMagica(AbstractBaseModel):
    nome = models.CharField(verbose_name="Criatura", null=False, blank=False, max_length=255)
    classificacao_MM = models.IntegerField(verbose_name="Classificação Ministério da Magia", null=False, blank=False, default=1, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    class Meta:
        verbose_name = 'criatura mágica'
        verbose_name_plural = 'criaturas mágicas'

class Mesa(MesaBase):
    class Meta:
        verbose_name = 'mesa'
        verbose_name_plural = 'mesas'