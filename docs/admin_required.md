# Protección de vistas administrativas con `admin_required`

## 1. ¿Qué es un decorador?

Un decorador es una función de Python que recibe otra función y añade comportamiento antes o después de ejecutarla, sin tener que modificar su código interno.

En Django se utiliza habitualmente para proteger vistas.

Una vista normal:

```python
def listar_usuarios(request):
    return render(request, 'admin/usuarios.html')
```

Una vista protegida:

```python
@admin_required
def listar_usuarios(request):
    return render(request, 'admin/usuarios.html')
```

Cuando Django recibe una petición para `listar_usuarios`, realmente ejecuta primero el decorador. El decorador decide si la petición puede continuar hasta la vista.

El flujo es:

```text
Petición del navegador
        ↓
admin_required
        ↓
¿Está autenticado?
        ↓
¿Está activo?
        ↓
¿Tiene rol ADMIN?
        ↓
Vista administrativa
```

> El nombre correcto es **decorador**. `decoder` es otra cosa y no describe esta funcionalidad.

## 2. Diferencia entre autenticación y autorización

Son conceptos relacionados, pero diferentes:

- **Autenticación:** comprueba quién es el usuario.
- **Autorización:** comprueba qué puede hacer ese usuario.

El login realiza la autenticación y comprueba que el usuario pueda entrar. El decorador `admin_required` añade autorización en cada vista interna.

Esto es importante porque un usuario podría intentar acceder directamente a una URL, por ejemplo:

```text
/usuarios/
/juegos/
/dashboard/
```

La aplicación no debe confiar solamente en que el usuario haya pasado por el formulario de login. Cada vista debe comprobar sus propios permisos.

## 3. Ubicación del decorador

El nombre recomendado sería:

```text
backend/backend_django/usuarios/decorators.py
```

`decorators.py` es el nombre habitual porque contiene decoradores. Si se cambia el nombre, también deben actualizarse todos los imports.

## 4. Implementación

El decorador puede implementarse así:
- decorators.py

```python
from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden

from .models import ModeloUsuarioModificado


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        if not request.user.is_active:
            return HttpResponseForbidden("Tu usuario está inactivo.")

        if request.user.rol != ModeloUsuarioModificado.Roles.ADMIN:
            return HttpResponseForbidden(
                "No tienes permisos para acceder a esta sección."
            )

        return view_func(request, *args, **kwargs)

    return wrapper
```

### Explicación paso a paso

### `wraps`

```python
from functools import wraps
```

`wraps` conserva el nombre y los metadatos de la vista original. Esto ayuda a Django, a las herramientas de depuración y a otros componentes del proyecto.

### `view_func`

```python
def admin_required(view_func):
```

`view_func` es la vista que queremos proteger.

Por ejemplo, cuando escribimos:

```python
@admin_required
def listar_usuarios(request):
    ...
```

Python envía `listar_usuarios` dentro de `admin_required` como `view_func`.

### `wrapper`

```python
def wrapper(request, *args, **kwargs):
```

`wrapper` es la nueva función que se ejecutará antes de la vista original. `*args` y `**kwargs` permiten que funcione tanto con vistas simples como con vistas que reciben parámetros de URL.

### Comprobación de autenticación

```python
if not request.user.is_authenticated:
    return redirect_to_login(request.get_full_path())
```

Si el usuario no ha iniciado sesión, se redirige al login. `request.get_full_path()` permite volver a la URL original después del login, si se configura ese flujo.

### Comprobación de usuario activo

```python
if not request.user.is_active:
    return HttpResponseForbidden("Tu usuario está inactivo.")
```

Aunque alguien tenga credenciales válidas, una cuenta desactivada no debe acceder al panel.

### Comprobación del rol

```python
if request.user.rol != ModeloUsuarioModificado.Roles.ADMIN:
```

Se utiliza la constante del modelo en lugar de escribir directamente `"ADMIN"`. Así se evita depender de un texto repetido y se mantiene la relación con las opciones oficiales del modelo.

### Ejecución de la vista

```python
return view_func(request, *args, **kwargs)
```

Solo se llega aquí cuando todas las comprobaciones anteriores han sido superadas.

## 5. Cómo utilizarlo en las vistas

Cada módulo que proteja vistas debe importar el decorador.

Si se renombra al nombre recomendado:

```python
from usuarios.decorators import admin_required
```

Después se aplica directamente sobre la vista:

```python
from usuarios.decorators import admin_required


@admin_required
def listar_usuarios(request):
    usuarios = ModeloUsuarioModificado.objects.all()
    return render(request, 'admin/usuarios.html', {
        'lista_usuarios': usuarios,
        'active_page': 'usuarios',
    })
```

Debe aplicarse a las vistas internas de:

- Dashboard.
- Usuarios.
- Juegos.
- Plataformas.
- Categorías.
- Ajustes.
- Perfil.
- Seguridad.
- Cambio de contraseña del administrador.
- Cierre de sesión del panel, si se desea restringirlo también.

## 6. Uso correcto del decorador actual

La implementación actual no recibe argumentos. Por tanto, debe usarse así:

```python
@admin_required
def mi_vista(request):
    ...
```

No debe usarse así:

```python
@admin_required(login_url='/')
def mi_vista(request):
    ...
```

Esa segunda forma intenta ejecutar `admin_required` inmediatamente con `login_url` como argumento, pero la función actual solo recibe `view_func`.

Si se necesita configurar el login, hay dos opciones:

1. Mantener el decorador sencillo y usar dentro de él la configuración de Django.
2. Convertirlo en un decorador configurable mediante una función externa.

Para este proyecto, la primera opción es suficiente y más fácil de mantener.

## 7. Respuestas esperadas

| Situación | Resultado |
|---|---|
| Usuario no autenticado | Redirección al login |
| Usuario autenticado pero inactivo | HTTP 403 |
| Usuario autenticado con rol `USER` | HTTP 403 |
| Usuario activo con rol `ADMIN` | Acceso permitido |

`403 Forbidden` significa que el servidor ha entendido la petición, pero el usuario no tiene permisos suficientes.

## 8. Decorador frente a middleware

Un middleware se ejecuta de forma global en las peticiones y respuestas de Django. Es apropiado para reglas generales de toda la aplicación, como sesiones, CSRF o seguridad.

Un decorador se aplica únicamente a las vistas que lo necesitan.

En este proyecto, el decorador es más adecuado porque existen diferentes zonas:

- Login público.
- Recuperación de contraseña.
- Futuras páginas del cliente.
- Panel administrativo.
- Futuras APIs de DRF.

Un middleware global podría bloquear por accidente páginas que no pertenecen al panel administrativo. Con `admin_required`, la intención queda explícita en cada vista.

## 9. Relación con el login

El login y `admin_required` cumplen responsabilidades diferentes:

```text
Login:
    Comprueba las credenciales y decide si el usuario puede iniciar sesión.

admin_required:
    Comprueba, en cada vista interna, que el usuario activo tenga rol ADMIN.
```

El login es la primera barrera. El decorador es la segunda barrera contra accesos directos por URL o peticiones manuales.

## 10. Relación con Django REST Framework

Las APIs que consumirá la página cliente no deberían protegerse con este decorador. DRF tiene su propio sistema de autenticación y permisos.

Para una API administrativa se recomienda crear un permiso:

```python
from rest_framework.permissions import BasePermission

from usuarios.models import ModeloUsuarioModificado


class IsAdminRole(BasePermission):
    message = "Solo los administradores pueden realizar esta acción."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.rol == ModeloUsuarioModificado.Roles.ADMIN
        )
```

Y utilizarlo en un ViewSet:

```python
from rest_framework.viewsets import ModelViewSet

from usuarios.permissions import IsAdminRole


class UsuarioViewSet(ModelViewSet):
    permission_classes = [IsAdminRole]
```

Resumen:

```text
Templates Django del panel → @admin_required
APIs de DRF                 → IsAdminRole
```

## 11. Comprobaciones manuales

Para verificar que la protección funciona:

1. Iniciar sesión como administrador.
2. Acceder al dashboard y a las vistas internas.
3. Cerrar sesión.
4. Intentar acceder directamente a `/dashboard/`.
5. Confirmar que se redirige al login.
6. Crear o utilizar un usuario con rol `USER`.
7. Iniciar sesión, si el flujo de la aplicación lo permite.
8. Intentar acceder directamente a `/usuarios/` o `/juegos/`.
9. Confirmar que se devuelve HTTP 403.
10. Desactivar un administrador.
11. Intentar acceder con esa cuenta.
12. Confirmar que se devuelve HTTP 403.

También se puede comprobar el proyecto con:

```bash
python manage.py check
```

## 12. Checklist de implementación

- [ ] Crear `usuarios/decorators.py`.
- [ ] Importar `admin_required` en cada módulo que lo utilice.
- [ ] Cambiar `@admin_required(login_url='/')` por `@admin_required` si se mantiene la implementación actual.
- [ ] Aplicar el decorador a todas las vistas internas.
- [ ] No aplicarlo al login ni al restablecimiento público de contraseña.
- [ ] Probar acceso como administrador.
- [ ] Probar acceso como usuario normal.
- [ ] Probar acceso con una cuenta desactivada.
- [ ] Ejecutar `python manage.py check`.
- [ ] Crear permisos separados para las APIs de DRF.
