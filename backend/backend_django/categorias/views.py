from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Categoria

@login_required(login_url='/')
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'admin/categorias.html', {
        'categorias': categorias,
        'active_page': 'categorias'
    })
