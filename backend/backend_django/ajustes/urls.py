# pyrefly: ignore [missing-import]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.mostrar_ajustes, name='mostrar_ajustes')
]