from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('<int:usuario_id>/editar', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:usuario_id>/', views.desactivar_usuario, name='desactivar_usuario'),
    path("enviar-correo/<int:user_id>/", views.enviar_correo_interno, name="enviar_correo_interno"),
    path("crear/", views.crear_usuario, name="crear_usuario"),
    path("definir-contrasena/<uidb64>/<token>/", views.definir_contrasena, name="definir_contrasena"),
]