import os
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from hbcommons.models import UsuarioAbstract as User, AbstractBaseModel

# Create your models here.
# TODO finalizar permissão de menus
class MenuItems(AbstractBaseModel):
    title = models.CharField(verbose_name='Título', null=False, blank=False, max_length=50)
    path = models.CharField(verbose_name='Caminho do menu', null=True, blank=True, max_length=50, help_text='Python/Django style')
    parent = models.ForeignKey(to='self', related_name='childs', blank=True, null=True, verbose_name='Item pai', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item de menu'
        verbose_name_plural  = 'itens de menu'

class MenuPerms(AbstractBaseModel):
    name = models.CharField(verbose_name='Nome', max_length=50, null=False, blank=False)
    items_permited = models.ManyToManyField(to=MenuItems, verbose_name='Itens liberados', blank=True, related_name='menu_perms')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'grupo de permissao de menu'
        verbose_name_plural  = 'grupos de permissões de menu'

class Usuario(User):
    permissions = models.ManyToManyField(to=MenuPerms, verbose_name='Permissões', blank=True, related_name='permissions_groups')
    def get_menuitens_perm(self):
        perms = []
        for p in self.permissions.all():
            for mi in p.items_permited.all():
                if mi.parent is None:
                    perms.append(self.return_menuitens_child_as_dict(mi))
        return perms

    def return_menuitens_child_as_dict(self, menuitem):
        childs = [self.return_menuitens_child_as_dict(c) for c in menuitem.childs.all()]
        return {str(menuitem.pk):{"title":menuitem.title,"path":menuitem.path, "childs" : childs}}

    def get_mesas_iniciadas(self):
        ret = []
        for x in self.fichas.all():
            if x.mesa and x.mesa.open_session:
                ret.append(x.mesa)
        return ret

    def is_mestre(self):
        return MesaBase.objects.filter(mestre=self).count() > 0

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class MesaBase(AbstractBaseModel, PolymorphicModel):
    name = models.CharField(verbose_name='Nome da mesa', null=False, blank=False, max_length=50)
    open_session = models.BooleanField(verbose_name='Sessão aberta', default=False, null=False, blank=False)
    mestre = models.ForeignKey(to=Usuario, on_delete=models.RESTRICT, verbose_name='Mestre', related_name='mesas_mestradas', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.open_session:
            for x in self.fichas_mesa.all():
                x.in_session = False
                x.save()
            self.mestre.in_session = False
            self.mestre.save()
        layer = get_channel_layer()
        for x in self.fichas_mesa.all():
            g_name = 'sessions_%s' % x.jogador.pk
            static_banner = ''
            alter = ''
            if self.get_content_type() == 'hp':
                static_banner = 'img/banners/hp.png'
                alter = "Harry Potter (Broomstix)"
            elif self.get_content_type() == 'coc':
                static_banner = 'img/banners/cthulhu.jpg'
                alter = "Call of Cthulhu (7e)"
            async_to_sync(layer.group_send)(
                g_name,
                {
                    'type': 'open_close_session',
                    'action': 'OPEN_SESSION' if self.open_session else 'CLOSE_SESSION',
                    'session_id': self.pk,
                    'session_name' : self.name,
                    'header' : {
                        'img' : os.path.join(settings.STATIC_URL, static_banner),
                        'alt' : alter
                    },
                    'link' : "#"
                }
            )
        super().save(*args, **kwargs)

    def is_mestre(self, user):
        return self.mestre == user

    def is_player(self, user):
        return self.fichas_mesa.filter(jogador=user).count() > 0

    def get_content_type(self):
        return ContentType.objects.get_for_id(self.polymorphic_ctype_id).app_label

    def __str__(self):
        return '{0} ({1}){2}'.format(self.name, self.get_content_type().upper(), ' - Aberta' if self.open_session else '')

class FichaBase(AbstractBaseModel, PolymorphicModel):
    nome_personagem = models.CharField(verbose_name='Nome do personagem', null=False, blank=False, max_length=50)
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fichas')
    mesa = models.ForeignKey(to=MesaBase, on_delete=models.RESTRICT, related_name='fichas_mesa', verbose_name='Mesa', null=True, blank=True)
    in_session = models.BooleanField("Está online na sessão", default=False, null=False, blank=False)

    def get_content_type(self):
        return ContentType.objects.get_for_id(self.polymorphic_ctype_id).app_label
