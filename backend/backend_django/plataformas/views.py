from django.shortcuts import render
from plataformas.models import Plataforma # importamos el modelo de app plataformas
from django.contrib.auth.decorators import login_required # para proteger las vistas
# Create your views here.
# renderizar la pagina plataformas.html, es decir, el html donde se muestran
@login_required
def mostrarPlataformas(request):
    plataformas = Plataforma.objects.all() # obtener TODAS las plataformas
    return render(request, 'admin/plataformas.html', {'plataformas': plataformas})

@login_required
# def para crear plataforma
# el id no es necesario porque se crea una nueva plataforma
# pedimos el tipo de plataforma (PC, PlayStation, Xbox, Nintendo)
def crearPlataforma(request):
    if request.method == 'POST':
        tipo = request.POST.get(tipo)
        plataforma = Plataforma.objects.create(
            tipo=tipo
        )
        plataforma.save() # guardamos la plataforma
    return render(request, 'admin/crearPlataforma.html')