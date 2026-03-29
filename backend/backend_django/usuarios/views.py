from django.shortcuts import render
from usuarios.models import ModeloUsuarioModificado

# Create your views here.
# def para devolver los usuarios de la base de datos
def listar_usuarios(request):
    lista_usuarios = ModeloUsuarioModificado.objects.all()
    return render(request, 'admin/usuarios.html', {'lista_usuarios': lista_usuarios})