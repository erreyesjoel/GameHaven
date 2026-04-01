from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
]
