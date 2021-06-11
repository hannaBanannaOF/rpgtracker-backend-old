from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rpg_tracker.coc.serializers import OcupationSerizalizer
from rpg_tracker.coc.models import Ocupation

# Create your views here.
class OcupationViewSet(viewsets.ModelViewSet):
    queryset = Ocupation.objects.all().order_by('-created_at')
    serializer_class = OcupationSerizalizer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']