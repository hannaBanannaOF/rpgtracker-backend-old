from django.urls import path
from . import views

app_name = 'api_coc'
urlpatterns = [
    path('ficha/<int:pk>', views.FichaDetails.as_view()),
]