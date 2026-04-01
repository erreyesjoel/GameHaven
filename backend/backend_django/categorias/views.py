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
    if request.method == 'POST':
        nombre = request.POST.get('nombre_categoria', '').strip()
        if not nombre:
            error = "El nombre de la categoría no puede estar vacío."
        elif Categoria.objects.filter(nombre_categoria=nombre).exists():
            error = "Esta categoría ya está registrada."
        else:
            Categoria.objects.create(nombre_categoria=nombre)
            return redirect('listar_categorias')

    return render(request, 'admin/crearCategoria.html', {
        'error': error,
        'active_page': 'categorias'
    })

@login_required(login_url='/')
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    error = None
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre_categoria', '').strip()
        if not nuevo_nombre:
            error = "El nombre de la categoría no puede estar vacío."
        elif Categoria.objects.exclude(id=categoria_id).filter(nombre_categoria=nuevo_nombre).exists():
            error = "Ya existe otra categoría con este nombre."
        else:
            categoria.nombre_categoria = nuevo_nombre
            categoria.save()
            return redirect('listar_categorias')

    return render(request, 'admin/editarCategoria.html', {
        'categoria': categoria,
        'error': error,
        'active_page': 'categorias'
    })

@login_required(login_url='/')
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')
