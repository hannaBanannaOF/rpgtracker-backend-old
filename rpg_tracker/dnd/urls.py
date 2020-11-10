from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = 'dnd'
urlpatterns = [
    path('racas', views.RaceDNDListView.as_view(), name='racas_list'),
    path('racas/<int:pk>', views.RaceDNDDetailView.as_view(), name='racas_details'),
    path('classes', views.ClasseDNDListView.as_view(), name='classes_list'),
    path('fichas/<int:pk>', views.ficha_detalhe, name='ficha_detalhe'),
]
