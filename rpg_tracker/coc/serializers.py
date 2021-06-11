from django.db.models import fields
from rest_framework import serializers
from .models import Ocupation

class OcupationSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocupation
        fields = ['pk', 'name']