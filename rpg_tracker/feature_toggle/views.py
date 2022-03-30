from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import FeatureToggle
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def feature_active(request):
    try:
        ft = FeatureToggle.objects.filter(feature=request.GET['feature'], active=True).first()
    except:
        ft = None
    if (ft is not None):
        return Response(True)
    return Response(False)