from django.urls import path
from django.urls.conf import include

app_name = 'api_v1'
urlpatterns = [
    path('accounts/', include('rpg_tracker.accounts.api_urls_v1', namespace='api_accounts_v1')),
    path('coc/', include('rpg_tracker.coc.api_urls_v1', namespace='api_coc_v1')),
    path('feature-toggle/', include('rpg_tracker.feature_toggle.api_urls_v1', namespace="api_ft_v1")),
]