from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from polymorphic.models import PolymorphicModel
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email inválido')
        u = self.model(email=self.normalize_email(email), **kwargs)
        u.set_password(password)
        u.save()
        return u

    def create_superuser(self, email, password, **kwargs):
        u = self.create_user(email, password, **kwargs)
        u.is_superuser = True
        u.save()
        return u

class AbstractBaseModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        
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

class Usuario(AbstractBaseUser, AbstractBaseModel):
    email = models.EmailField('Email', unique=True, blank=False, null=False)
    password = models.CharField('Senha', blank=False, null=False, max_length=250)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField('Nome', max_length=100, blank=False, null=False)
    last_name = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    is_superuser = models.BooleanField('Superusuário', default=False)
    permissions = models.ManyToManyField(to=MenuPerms, verbose_name='Permissões', blank=True, related_name='permissions_groups')

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def fullname(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

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

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class FichaBase(AbstractBaseModel, PolymorphicModel):
    nome_personagem = models.CharField(verbose_name='Nome do personagem', null=False, blank=False, max_length=50)
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fichas')

    def get_content_type(self):
        return ContentType.objects.get_for_id(self.polymorphic_ctype_id).app_label

class MesaBase(AbstractBaseModel, PolymorphicModel):
    name = models.CharField(verbose_name='Nome da mesa', null=False, blank=False, max_length=50)
    open_session = models.BooleanField(verbose_name='Sessão aberta', default=False, null=False, blank=False)
    mestre = models.ForeignKey(to=Usuario, on_delete=models.RESTRICT, verbose_name='Mestre', related_name='mesas_mestradas', blank=True, null=True)

    def is_mestre(self, user):
        return self.mestre == user
        
    def get_content_type(self):
        return ContentType.objects.get_for_id(self.polymorphic_ctype_id).app_label

    def __str__(self):
        return '{0} ({1}){2}'.format(self.name, self.get_content_type().upper(), ' - Aberta' if self.open_session else '')

class FichaInMesa(AbstractBaseModel):
    ficha = models.ForeignKey(to=FichaBase, verbose_name='Ficha', related_name='mesas_jogadas', on_delete=models.CASCADE, blank=False, null=False)
    mesa = models.ForeignKey(to=MesaBase, verbose_name='Mesa', related_name='fichas', null=False, blank=False, on_delete=models.CASCADE)
    in_session = models.BooleanField(verbose_name='Está online', default=False, blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.mesa.get_content_type != self.ficha.get_content_type:
            raise Exception
        super().save(*args, **kwargs)

    def is_player_in_mesa(self, player):
        for x in self.mesa.fichas.all():
            if x.ficha.jogador == player:
                return True
            
        return False

    def __str__(self):
        return '{0} em {1}'.format(self.ficha.nome_personagem, self.mesa.name)