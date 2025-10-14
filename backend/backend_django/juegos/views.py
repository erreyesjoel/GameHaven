from django.shortcuts import render
from juegos.models import Juego # importamos el modelo
from plataformas.models import Plataforma # importamos el modelo

# Create your views here.
# renderizar juegos.html y funcion para devolver los juegos
def mostrarJuegos(request):
    juegos = Juego.objects.all() # obtenemos todos los juegos
    plataformas = Plataforma.objects.all() # obtenemos todas las plataformas
    return render(request, 'admin/juegos.html', {'juegos': juegos, 'plataformas': plataformas})