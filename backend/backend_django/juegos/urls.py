from django.urls import path # importamos path, para definir las rutas
from . import views # importamos las vistas del mismo directorio, osea de nuestra app (juegos)

urlpatterns = [
    path('', views.mostrarJuegos, name='mostrar_juegos'),
    path('eliminar/<int:juego_id>/', views.eliminarJuego, name='eliminar_juego'),
]