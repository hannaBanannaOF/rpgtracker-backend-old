from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = 'dnd'
urlpatterns = [
    path('racas', views.RaceDNDListView.as_view(), name='racas_list'),
    path('racas/<int:pk>', views.RaceDNDDetailView.as_view(), name='racas_details'),
    path('classes', views.ClasseDNDListView.as_view(), name='classes_list'),
    path('classes/<int:pk>', views.ClasseDNDDetailView.as_view(), name='classes_details'),
    path('fichas/<int:pk>', views.ficha_detalhe, name='ficha_detalhe'),
    path('decks/gm_crit', views.get_deck_gm_crit, name='gm_crit_deck'),
    path('decks/player_crit', views.get_deck_player_crit, name='player_crit_deck'),
    path('decks/fail', views.get_deck_fail, name='fail_deck'),
    path('decks/gm_crit/get_card', views.deck_gm_crit_card, name='gm_crit_deck_get_card'),
    path('decks/player_crit/get_card', views.deck_player_crit_card, name='player_crit_deck_get_card'),
    path('decks/fail/get_card', views.deck_fail_card, name='fail_deck_get_card')
]



