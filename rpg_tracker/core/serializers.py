from rest_framework import serializers
from rpg_tracker.core.models import FichaBase, MesaBase
from rpg_tracker.core.models import Usuario 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email','first_name', 'last_name', 'nickname', 'photo', 'is_mestre')

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaBase
        fields = ('id', 'nome_personagem', 'get_content_type', 'mesa', 'jogador')
        depth = 1

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaBase
        fields = ('id', 'name', 'get_content_type', 'open_session', 'fichas_mesa')
        depth = 2