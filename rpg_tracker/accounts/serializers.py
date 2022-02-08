from rest_framework import serializers
from rpg_tracker.core.models import Usuario 


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('email','first_name', 'last_name', 'nickname')