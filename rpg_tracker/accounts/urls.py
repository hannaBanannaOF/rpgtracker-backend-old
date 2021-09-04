from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    path('fichas', views.fichas, name='fichas'),
]
