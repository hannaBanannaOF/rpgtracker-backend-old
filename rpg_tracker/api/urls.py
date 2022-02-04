from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api'
urlpatterns = [
    path('v1/token/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/token/social-auth/', include('rest_social_auth.urls_jwt_pair')),
    path('v1/', include('rpg_tracker.api.url_v1', namespace='api_v1')),
]