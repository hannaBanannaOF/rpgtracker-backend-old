from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rpg_tracker.core.models import Usuario


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('email',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    class Meta:
        model = Usuario
        fields = ('token', 'email', 'password')