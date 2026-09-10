from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import ModeloUsuarioModificado
from django.contrib.auth.decorators import login_required
from .emails import send_internal_email
from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import login

# Create your views here.
# def para devolver los usuarios de la base de datos
@login_required
def listar_usuarios(request):
    lista_usuarios = ModeloUsuarioModificado.objects.all().order_by('-id')
    return render(request, 'admin/usuarios.html', {'lista_usuarios': lista_usuarios, 'active_page': 'usuarios'})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        rol = request.POST.get('rol')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Crear el usuario sin contraseña definida (se le asigna una aleatoria o se deja pendiente)
        usuario = ModeloUsuarioModificado.objects.create(
            username=username,
            email=email,
            rol=rol,
            first_name=first_name,
            last_name=last_name,
            is_active=True # Lo activamos para que pueda resetear pass
        )
        usuario.set_unusable_password() # No password yet
        usuario.save()

        # Enviar el correo para definir contraseña
        send_internal_email(request, usuario)

        return redirect('listar_usuarios')

    return render(request, 'admin/crearUsuario.html', {
        'roles': ModeloUsuarioModificado.Roles.choices,
        'active_page': 'usuarios'
    })

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

def enviar_correo_interno(request, user_id):
    user = get_object_or_404(ModeloUsuarioModificado, pk=user_id)

    send_internal_email(request, user)

    return JsonResponse({"status": "ok", "message": "Correo enviado"})

def definir_contrasena(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = ModeloUsuarioModificado.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, ModeloUsuarioModificado.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                # Opcional: loguear al usuario después de cambiar la contraseña
                login(request, user)
                return redirect('admin_dashboard') # O a donde prefieras
        else:
            form = SetPasswordForm(user)
        
        return render(request, 'autenticacion/internal_set_password.html', {
            'form': form,
            'validlink': True
        })
    else:
        return render(request, 'autenticacion/internal_set_password.html', {
            'validlink': False
        })