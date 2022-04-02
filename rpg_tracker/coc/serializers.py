from dataclasses import fields
from rest_framework import serializers
from rpg_tracker.core.serializers import UserSerializer
from .models import Ocupation, FichaCOC, WeaponsInFicha, Weapons, Skills

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapons
        exclude = ['ammo', 'skill_used']

class ArmaEmFichaSerializer(serializers.ModelSerializer):
    weapon = ArmaSerializer()
    class Meta:
        model = WeaponsInFicha
        fields = ['id', 'weapon', 'ammo_left', 'rounds_left', 'nickname', 'normal_success_value', 'total_ammo_left']
        depth = 1

class FichaCOCSerializer(serializers.ModelSerializer):
    jogador = UserSerializer()
    weapons = ArmaEmFichaSerializer(many=True)
    class Meta:
        model = FichaCOC
        fields =  ['age', 'birthplace', 'residence', 'sex', 'nome_personagem', 'jogador', 'pulp_cthulhu', 'pulp_archetype',
                    'strength', 'constitution', 'size', 'dexterity', 'appearence', 'inteligence', 'power', 'education', 'move_rate',
                    'skill_list', 'hp', 'max_hp', 'major_wound', 'san', 'max_san', 'start_san', 'temporary_insanity', 
                    'indefinity_insanity', 'luck', 'max_mp', 'mp', 'weapons', 'pulp_talents', 'dodge', 'build', 'bonus_dmg', 'ocupation']
        depth = 1

class OcupationSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocupation
        fields = ['pk', 'name']