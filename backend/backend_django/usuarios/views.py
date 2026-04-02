from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import ModeloUsuarioModificado
from django.contrib.auth.decorators import login_required

# Create your views here.
# def para devolver los usuarios de la base de datos
@login_required
def listar_usuarios(request):
    lista_usuarios = ModeloUsuarioModificado.objects.all()
    return render(request, 'admin/usuarios.html', {'lista_usuarios': lista_usuarios, 'active_page': 'usuarios'})

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(ModeloUsuarioModificado, id=usuario_id)
    if request.method == 'POST':
        usuario.username = request.POST.get('username', usuario.username)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.rol = request.POST.get('rol', usuario.rol)
        usuario.first_name = request.POST.get('first_name', usuario.first_name)
        usuario.last_name = request.POST.get('last_name', usuario.last_name)
        usuario.save()
        return redirect('listar_usuarios')
    
    return render(request, 'admin/editarUsuario.html', {
        'usuario': usuario,
        'roles': ModeloUsuarioModificado.Roles.choices,
        'active_page': 'usuarios'
    })

@login_required
def desactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(ModeloUsuarioModificado, id=usuario_id)
    usuario.is_active = False
    usuario.save()
    return redirect('listar_usuarios')