from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

routerCoc = routers.DefaultRouter()
routerCoc.register(r'ocupations', views.OcupationViewSet)

app_name = 'api'
urlpatterns = [
    path('coc/', include(routerCoc.urls)),
]