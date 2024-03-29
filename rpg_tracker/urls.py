"""rpg_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('rpg_tracker.core.urls', namespace='core')),
    path('conta/', include('rpg_tracker.accounts.urls', namespace='accounts')),
    path('coc/', include('rpg_tracker.coc.urls', namespace='coc')),
    path('hp/', include('rpg_tracker.hp.urls', namespace='hp')),
    #path('dnd/', include('rpg_tracker.dnd.urls', namespace='dnd')),
    path('admin/', admin.site.urls),
    path('api/', include('rpg_tracker.api.urls', namespace='api')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]