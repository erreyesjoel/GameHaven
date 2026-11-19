from django.contrib.auth.forms import PasswordResetForm

from .models import ModeloUsuarioModificado


class AdminPasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        usuarios = ModeloUsuarioModificado.objects.filter(
            email__iexact=email,
            is_active=True,
            rol=ModeloUsuarioModificado.Roles.ADMIN,
        )

        return (
            usuario for usuario in usuarios
            if usuario.has_usable_password() and usuario.email
        )