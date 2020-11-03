from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from polymorphic.models import PolymorphicModel

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

class Usuario(AbstractBaseUser, AbstractBaseModel):
    email = models.EmailField('Email', unique=True, blank=False, null=False)
    password = models.CharField('Senha', blank=False, null=False, max_length=250)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField('Nome', max_length=100, blank=False, null=False)
    last_name = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    is_superuser = models.BooleanField('Superusuário', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class FichaBase(AbstractBaseModel, PolymorphicModel):
    nome_personagem = models.CharField(verbose_name='Nome do personagem', null=False, blank=False, max_length=50)
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fichas')