from rest_framework import serializers
from rpg_tracker.core.models import FichaBase, MesaBase

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaBase
        fields = ('id', 'nome_personagem', 'get_content_type', 'mesa')
        depth = 1

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaBase