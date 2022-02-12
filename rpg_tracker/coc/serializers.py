from rest_framework import serializers
from rpg_tracker.core.serializers import UserSerializer
from .models import Ocupation, FichaCOC

class FichaCOCSerializer(serializers.ModelSerializer):
    jogador = UserSerializer()
    
    class Meta:
        model = FichaCOC
        fields =  ['age', 'birthplace', 'residence', 'sex', 'nome_personagem', 'jogador', 'pulp_cthulhu', 'pulp_archetype',
                    'strength', 'constitution', 'size', 'dexterity', 'appearence', 'inteligence', 'power', 'education', 'move_rate',
                    'get_skill_list_as_array']
        depth = 1

class OcupationSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocupation
        fields = ['pk', 'name']