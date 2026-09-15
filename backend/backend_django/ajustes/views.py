# pyrefly: ignore [missing-import]
from django.shortcuts import redirect, render
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
# def para mostrar la pagina de ajustes
# pyrefly: ignore [missing-signature]
@login_required
def mostrar_ajustes(request):
    return render(request, 'admin/ajustes.html', {'active_page': 'ajustes'})


@login_required
def seguridad(request):
    return render(request, 'admin/seguridad.html', {'active_page': 'ajustes'})


@login_required
def perfil(request):
    usuario = request.user

    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name', '').strip()
        usuario.last_name = request.POST.get('last_name', '').strip()
        usuario.email = request.POST.get('email', '').strip()
        usuario.save(update_fields=['first_name', 'last_name', 'email'])
        return redirect('perfil_admin')

    return render(request, 'admin/perfil.html', {
        'usuario': usuario,
        'active_page': 'ajustes',
    })


@login_required
def cambiar_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        usuario = form.save()
        update_session_auth_hash(request, usuario)
        return redirect('seguridad_admin')

    return render(request, 'admin/cambiarPassword.html', {
        'form': form,
        'active_page': 'ajustes',
    })