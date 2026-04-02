from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('<int:usuario_id>/editar', views.editar_usuario, name='editar_usuario'),
]