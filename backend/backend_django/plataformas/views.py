from django.shortcuts import render, redirect, get_object_or_404 # importamos render para renderizar templates y redirect para redirigir, get_object_or_404 para obtener objetos o devolver 404
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

@login_required
# def para editar plataforma
def editarPlataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id) # buscamos plataforma por id
    plataformas = Plataforma.objects.all() # obtenemos todas las plataformas, y las mostramos en la vista / pagina
    if request.method == 'POST':
        plataforma.tipo = request.POST.get('tipo', plataforma.tipo) # obtenemos el tipo de plataforma
        plataforma.save() # guardamos los cambios
        return redirect('mostrar_plataformas') # redirigimos a la lista de plataformas
    return render(request, 'admin/editarPlataforma.html', 
    {'plataforma': plataforma, 
    'plataformas': plataformas
    })