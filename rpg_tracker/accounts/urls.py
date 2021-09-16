from os import name
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('fichas', views.fichas, name='fichas'),
    path('user/<int:pk>', views.user_infos, name='user-info')
]
