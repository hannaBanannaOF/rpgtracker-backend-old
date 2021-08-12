from django.urls import path
from . import views

app_name = 'hp'
urlpatterns = [
    path('ficha/<int:pk>', views.ficha, name='ficha'),
]