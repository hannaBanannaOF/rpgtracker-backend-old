from django.urls import path
from . import views

app_name = 'api_ft'
urlpatterns = [
    path('active/', views.feature_active),
]