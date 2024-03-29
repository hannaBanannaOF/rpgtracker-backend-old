from rpg_tracker.core.forms import UsuarioForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from rpg_tracker.core.models import FichaBase, Usuario
from django.views.generic import DetailView
from rpg_tracker.core.forms import UsuarioForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rpg_tracker.core.serializers import UserSerializer, FichaSerializer, MesaSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
@api_view(['GET'])
@login_required
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class MinhasFichasView(ListAPIView):
    serializer_class = FichaSerializer
    def get_queryset(self):
        user = self.request.user
        return user.fichas.all()

class MinhasMesasMestradasView(ListAPIView):
    serializer_class = MesaSerializer
    def get_queryset(self):
        user = self.request.user
        return user.mesas_mestradas.all()

############################ NO API CALLS ###############################
@login_required
def fichas(request):
    ctx = {}
    if request.user.is_superuser:
        ctx['fichas'] = FichaBase.objects.all()
    else:
        ctx['fichas'] = request.user.fichas.all()
        if request.user.is_mestre():
            ctx['mestradas'] = FichaBase.mesa.filter(mestre=request.user).all()
    return render(request, 'fichas.html', ctx)

class UserInfoDetailView(DetailView):
    model = Usuario
    context_object_name = 'user'
    template_name = 'user-infos.html'

    user = None

    def get(self, request, *args, **kwargs):
        if(kwargs.get('pk') != request.user.pk and not request.user.is_superuser):
            raise PermissionDenied
        self.user = get_object_or_404(Usuario, pk=kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['user_form'] = UsuarioForm(instance=self.user)
        return ctx

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST or None, instance=self.get_object())
        if form.is_valid():
            self.object = form.save()
        else:    
            self.object = self.get_object()
        ctx = self.get_context_data(object=self.object)
        ctx['user_form'] = UsuarioForm(instance=self.object)
        return self.render_to_response(ctx)
        
user_infos = login_required(UserInfoDetailView.as_view())