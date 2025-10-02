from django.core.management.base import BaseCommand  # Importa la clase base para comandos personalizados de Django
from usuarios.models import ModeloUsuarioModificado  # Importa el modelo de usuario personalizado

class Command(BaseCommand):
    help = 'Crea el usuario admin inicial y un usuario normal'  # Descripción del comando, aparece con --help

    def handle(self, *args, **options):
        # Verifica si el usuario 'havengame' ya existe
        if not ModeloUsuarioModificado.objects.filter(username='havengame').exists():
            # Si no existe, lo crea con los datos especificados y rol ADMIN
            ModeloUsuarioModificado.objects.create_user(
                username='havengame',
                password='hav#nGame!',
                email='havengame@gmail.com',
                rol=ModeloUsuarioModificado.Roles.ADMIN
            )
            self.stdout.write(self.style.SUCCESS("Usuario 'havengame' creado exitosamente."))
        else:
            self.stdout.write(self.style.WARNING("El usuario 'havengame' ya existe."))

        # Verifica si el usuario 'usuario1' ya existe
        if not ModeloUsuarioModificado.objects.filter(username='usuario1').exists():
            # Si no existe, lo crea con los datos especificados y rol USER
            ModeloUsuarioModificado.objects.create_user(
                username='usuario1',
                password='usuario123',
                email='usuario1@gmail.com',
                rol=ModeloUsuarioModificado.Roles.USER
            )
            self.stdout.write(self.style.SUCCESS("Usuario 'usuario1' creado exitosamente."))
        else:
            self.stdout.write(self.style.WARNING("El usuario 'usuario1' ya existe."))