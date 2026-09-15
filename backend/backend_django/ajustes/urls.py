# pyrefly: ignore [missing-import]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_ajustes, name='mostrar_ajustes'),
    path('perfil/', views.perfil, name='perfil_admin'),
    path('seguridad/', views.seguridad, name='seguridad_admin'),
    path('seguridad/cambiar-password/', views.cambiar_password, name='cambiar_password'),
]