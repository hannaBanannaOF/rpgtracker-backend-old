from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = 'dnd'
urlpatterns = [
    path('<int:pk>', views.ficha_detalhe, name='ficha_detalhe'),
    # path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'),
    # path('offline', views.offline, name='offline')
]