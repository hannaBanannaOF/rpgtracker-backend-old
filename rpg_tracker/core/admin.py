from django.contrib import admin
from .models import Usuario, MenuItems, MenuPerms
# Register your models here.

admin.site.register([Usuario, MenuItems, MenuPerms])