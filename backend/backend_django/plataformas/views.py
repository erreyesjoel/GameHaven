from django.shortcuts import render
from plataformas.models import Plataforma # importamos el modelo de app plataformas
from django.contrib.auth.decorators import login_required # para proteger las vistas
# Create your views here.
# renderizar la pagina plataformas.html, es decir, el html donde se muestran
@login_required
def mostrarPlataformas(request):
    plataformas = Plataforma.objects.all() # obtener TODAS las plataformas
    return render(request, 'admin/plataformas.html', {'plataformas': plataformas})