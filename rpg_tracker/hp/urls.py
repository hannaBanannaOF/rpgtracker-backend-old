from django.urls import path
from . import views

app_name = 'hp'
urlpatterns = [
    path('ficha/<int:pk>', views.ficha, name='ficha'),
    path('ficha/<int:pk>/folio-universitas', views.folio_universitas_ficha, name="folio_universitas_ficha"),
    path('folio-universitas', views.folio_universitas, name="folio_universitas"),
    path('folio-universitas/<int:pk>/cartas', views.folio_universitas_cartas, name="folio_universitas_cartas")
]