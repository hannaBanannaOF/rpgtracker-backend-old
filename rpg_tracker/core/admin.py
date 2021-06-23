from django.contrib import admin
from .models import Usuario, MenuItems, MenuPerms, FichaInMesa
# Register your models here.

admin.site.register([Usuario, MenuItems, MenuPerms, FichaInMesa])