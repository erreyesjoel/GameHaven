from django.shortcuts import render, redirect, get_object_or_404 # importamos render para renderizar templates y redirect para redirigir, get_object_or_404 para obtener objetos o devolver 404
from plataformas.models import Plataforma # importamos el modelo de app plataformas
from django.contrib.auth.decorators import login_required # para proteger las vistas
import re

# Create your views here.
# renderizar la pagina plataformas.html, es decir, el html donde se muestran
@login_required
def mostrarPlataformas(request):
    plataformas = Plataforma.objects.all() # obtener TODAS las plataformas
    return render(request, 'admin/plataformas.html', {'plataformas': plataformas, 'active_page': 'plataformas'})

@login_required
# def para crear plataforma
# el id no es necesario porque se crea una nueva plataforma
# pedimos el tipo de plataforma (PC, PlayStation, Xbox, Nintendo)
def crearPlataforma(request):
    error = None
    if request.method == 'POST':
        tipo = request.POST.get('tipo', '').strip()
        # Normalizar: quitar espacios extra y poner todo en minúsculas para comparar
        tipo_normalizado = re.sub(r'\s+', '', tipo).lower()
        # Buscar si ya existe una plataforma con ese tipo normalizado
        plataformas = Plataforma.objects.all()
        for p in plataformas:
            if re.sub(r'\s+', '', p.tipo).lower() == tipo_normalizado:
                error = "Ya existe una plataforma con ese nombre (aunque varíen los espacios o mayúsculas)."
                return render(request, 'admin/crearPlataforma.html', {'error': error})
        plataforma = Plataforma.objects.create(tipo=tipo)
        plataforma.save() # guardamos la plataforma
        return redirect('mostrar_plataformas')
    return render(request, 'admin/crearPlataforma.html')

@login_required
# def para editar plataforma
def editarPlataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    error = None
    if request.method == 'POST':
        nuevo_tipo = request.POST.get('tipo', plataforma.tipo).strip()
        nuevo_tipo_normalizado = re.sub(r'\s+', '', nuevo_tipo).lower()
        plataformas = Plataforma.objects.exclude(id=plataforma.id)
        for p in plataformas:
            if re.sub(r'\s+', '', p.tipo).lower() == nuevo_tipo_normalizado:
                error = "Ya existe una plataforma con ese nombre (aunque varíen los espacios o mayúsculas)."
                return render(request, 'admin/editarPlataforma.html', {
                    'plataforma': plataforma,
                    'error': error
                })
        plataforma.tipo = nuevo_tipo
        plataforma.save()
        return redirect('mostrar_plataformas')
    return render(request, 'admin/editarPlataforma.html', {
        'plataforma': plataforma,
        'error': error
    })

@login_required
# def para eliminar una plataforma
def eliminarPlataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    plataforma.delete() # eliminamos la plataforma
    return redirect('mostrar_plataformas') # redirigimos a la lista de plataformas