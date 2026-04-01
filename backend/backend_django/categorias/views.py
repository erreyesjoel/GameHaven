from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria

@login_required(login_url='/')
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'admin/categorias.html', {
        'categorias': categorias,
        'active_page': 'categorias'
    })

@login_required(login_url='/')
def crear_categoria(request):
    error = None
    # Obtener todas las opciones posibles definidas en el modelo
    todas_opciones = Categoria.Categorias.choices
    # Obtener las categorías que ya existen en la BD
    existentes = Categoria.objects.values_list('nombre_categoria', flat=True)
    # Filtrar opciones disponibles (las que no están en la BD)
    opciones_disponibles = [opt for opt in todas_opciones if opt[0] not in existentes]

    if request.method == 'POST':
        nombre = request.POST.get('nombre_categoria')
        if not nombre:
            error = "Debes seleccionar una categoría."
        elif Categoria.objects.filter(nombre_categoria=nombre).exists():
            error = "Esta categoría ya está registrada."
        else:
            Categoria.objects.create(nombre_categoria=nombre)
            return redirect('listar_categorias')

    return render(request, 'admin/crearCategoria.html', {
        'opciones': opciones_disponibles,
        'error': error,
        'active_page': 'categorias'
    })

@login_required(login_url='/')
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    error = None
    # Todas las opciones posibles
    todas_opciones = Categoria.Categorias.choices
    # Existentes menos la actual
    existentes = Categoria.objects.exclude(id=categoria_id).values_list('nombre_categoria', flat=True)
    # Opciones disponibles (incluye la actual)
    opciones_disponibles = [opt for opt in todas_opciones if opt[0] not in existentes]

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre_categoria')
        if not nuevo_nombre:
            error = "Debes seleccionar una categoría."
        elif Categoria.objects.exclude(id=categoria_id).filter(nombre_categoria=nuevo_nombre).exists():
            error = "Esta categoría ya está siendo usada por otra entrada."
        else:
            categoria.nombre_categoria = nuevo_nombre
            categoria.save()
            return redirect('listar_categorias')

    return render(request, 'admin/editarCategoria.html', {
        'categoria': categoria,
        'opciones': opciones_disponibles,
        'error': error,
        'active_page': 'categorias'
    })

@login_required(login_url='/')
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')
