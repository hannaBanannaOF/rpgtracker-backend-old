from rest_framework.permissions import BasePermission

class ViewFicha(BasePermission):
    message = 'Você não tem permissão para ver essa ficha!'

    def has_object_permission(self, request, view, obj):
        return (obj.mesa and obj.mesa.is_mestre(request.user)) or obj.jogador == request.user or request.user.is_superuser