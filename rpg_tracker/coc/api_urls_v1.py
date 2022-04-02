from django.urls import path
from . import views

app_name = 'api_coc'
urlpatterns = [
    path('ficha/details/', views.FichaDetails.as_view()),
]