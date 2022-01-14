from django.urls import path
from django.urls.conf import include
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'api'
urlpatterns = [
    path('accounts/', include('rpg_tracker.accounts.api_urls', namespace='api_accounts')),
    path('token-auth/', obtain_jwt_token),
]