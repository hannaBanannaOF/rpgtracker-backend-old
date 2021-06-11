from django.db import models
from django.contrib.auth import get_user_model
from rpg_tracker.core.models import AbstractBaseModel

User = get_user_model()

# Create your models here.
class PasswordReset(AbstractBaseModel):
    pass