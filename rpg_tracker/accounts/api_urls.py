from django.urls import path
from . import views

app_name = 'api_accounts'
urlpatterns = [
    path('current-user', views.current_user),
]