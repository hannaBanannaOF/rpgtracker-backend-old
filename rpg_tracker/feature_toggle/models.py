from tabnanny import verbose
from django.db import models
from django.db.models.enums import TextChoices
from hbcommons.models import AbstractBaseModel

# Create your models here.
class FeatureToggle(AbstractBaseModel):
    class FeatureChoices(TextChoices):
        NEW_LOGIN = "NEW_LOGIN", "Novo login"

    feature = models.CharField("Feature", max_length=45, choices=FeatureChoices.choices, null=False, blank=False)
    active = models.BooleanField("Ativo", default=False, null=False, blank=False)

    def __str__(self):
        return "{0}({1})".format(self.feature, self.active)

    class Meta:
        verbose_name = "Feature toggle"
        verbose_name_plural = "Features toggle"