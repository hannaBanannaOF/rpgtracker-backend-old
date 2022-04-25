from django.urls import path
from . import views

app_name = 'api_accounts'
urlpatterns = [
    path('current-user', views.current_user),
    path('current-user/fichas', views.MinhasFichasView.as_view()),
    path('current-user/mesas-mestradas', views.MinhasMesasMestradasView.as_view()),
]