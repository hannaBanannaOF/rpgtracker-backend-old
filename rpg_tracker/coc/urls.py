from django.urls import path
from . import views

app_name = 'coc'
urlpatterns = [
    path('ficha/<int:pk>', views.ficha, name='ficha'),
]