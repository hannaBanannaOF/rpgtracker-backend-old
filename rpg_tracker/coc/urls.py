from django.urls import path
from . import views

app_name = 'coc'
urlpatterns = [
    path('ficha/<int:pk>', views.ficha, name='ficha'),
    path('skills', views.skill_list, name='skill_list'),
    path('skills/<int:pk>', views.skill_detail, name='skill_detail'),
]