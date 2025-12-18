from django.urls import path # importamos path, para definir las rutas
from . import views # importamos las vistas del mismo directorio, osea de nuestra app (plataformas)

urlpatterns = [
    path('', views.mostrarPlataformas, name='mostrar_plataformas'), # se deja vacia porque es la ruta principal de app plataformas
]