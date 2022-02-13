from rest_framework import serializers
from rpg_tracker.core.serializers import UserSerializer
from .models import Ocupation, FichaCOC

class FichaCOCSerializer(serializers.ModelSerializer):
    jogador = UserSerializer()
    
    class Meta:
        model = FichaCOC
        fields =  ['age', 'birthplace', 'residence', 'sex', 'nome_personagem', 'jogador', 'pulp_cthulhu', 'pulp_archetype',
                    'strength', 'constitution', 'size', 'dexterity', 'appearence', 'inteligence', 'power', 'education', 'move_rate',
                    'get_skill_list_as_array', 'hp', 'max_hp', 'major_wound', 'san', 'max_san', 'start_san', 'temporary_insanity', 
                    'indefinity_insanity', 'luck', 'max_mp', 'mp', 'weapons', 'pulp_talents', 'dodge', 'build', 'bonus_dmg']
        depth = 1

class OcupationSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocupation
        fields = ['pk', 'name']