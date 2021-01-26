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
    path('decks/fail/get_card', views.deck_fail_card, name='fail_deck_get_card'),
    path('traps/1_4',views.traps_1_4,name='1_4_traps'),
    path('traps/1_4/get',views.traps_1_4_get,name='get_1_4_traps'),
    path('traps/5_8',views.traps_5_8,name='5_8_traps'),
    path('traps/5_8/get',views.traps_5_8_get,name='get_5_8_traps'),
    path('traps/9_12',views.traps_9_12,name='9_12_traps'),
    path('traps/9_12/get',views.traps_9_12_get,name='get_9_12_traps'),
    path('traps/13_16',views.traps_13_16,name='13_16_traps'),
    path('traps/13_16/get',views.traps_13_16_get,name='get_13_16_traps'),
    path('traps/17_20',views.traps_17_20,name='17_20_traps'),
    path('traps/17_20/get',views.traps_17_20_get,name='get_17_20_traps')
]



