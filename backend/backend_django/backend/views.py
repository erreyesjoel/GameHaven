from django.shortcuts import render # importante para renderizar plantillas como html
from django.contrib.auth.decorators import login_required  # necesario para proteger vistas privadas
from usuarios.models import ModeloUsuarioModificado  # importar el modelo de usuario personalizado
from django.contrib.auth import authenticate, login  # para autenticar y loguear usuarios
from django.shortcuts import render, redirect  # importante para renderizar plantillas y redirigir
from django.contrib.auth import logout  # para cerrar sesion

# def para renderizar el template de login
def login_template(request):
    # si el usuario esta autenticado, redirigir al dashboard
    # para que si esta autenticado, que no pueda volver al login sin cerrar sesion
    if request.user.is_authenticated:
        return redirect('admin_dashboard_template')
    error = None
    if request.method == 'POST':
        # cogemos los campos email y password
        email = request.POST.get('email')
        password = request.POST.get('password')
        # buscar el usuario por email
        try:
            user_obj = ModeloUsuarioModificado.objects.get(email=email)
            # autenticar usando el username del usuario encontrado
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None: # si el usuario es valido, osea sus credenciales son correctas, logeamos
                login(request, user)  # loguear al usuario
                return redirect('admin_dashboard_template')  # redirigir al dashboard de admin
            else:
                error = "Credenciales inválidas. Por favor, inténtalo de nuevo."
        except ModeloUsuarioModificado.DoesNotExist:
            error = "Credenciales inválidas. Por favor, inténtalo de nuevo."
    # si no es post, renderizamos el template de login
    return render(request, 'autenticacion/login.html', {'error': error})

# def para renderiz el dashboard de admin al logearnos en django admin (template)
@login_required(login_url='/')  # redirige al login si no está autenticado, por eso @login_required
def admin_dashboard_template(request):
    # con esto, podriamos pasar datos al template, como el nombre del usuario o el email
    # en el html se accede con {{ user.username }} o {{ user.email }}
    # no hace falta pasar el user, porque django lo pasa automaticamente con el request y  por django contrib.auth.context_processors.auth
    return render(request, 'admin/dashboardAdmin.html')

# def para logout en django template
@login_required(login_url='/')  # redirige al login si no está autenticado, por eso @login_required
def logout_view(request):
    logout(request)  # cerrar sesion
    return redirect('login_template')  # redirigir al login
