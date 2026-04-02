from django.core.management.base import BaseCommand
from usuarios.models import ModeloUsuarioModificado

class Command(BaseCommand):
    help = 'Crea usuarios iniciales para pruebas (admin + varios usuarios normales)'

    def handle(self, *args, **options):

        usuarios = [
            # ADMIN
            {
                'username': 'havengame',
                'password': 'hav#nGame!',
                'email': 'havengame@gmail.com',
                'rol': ModeloUsuarioModificado.Roles.ADMIN
            },

            # USUARIOS NORMALES (rol por defecto)
            {
                'username': 'usuario1',
                'password': 'usuario123',
                'email': 'usuario1@gmail.com',
            },
            {
                'username': 'stu',
                'password': 'stu123!',
                'first_name': 'stu',
                'last_name': 'macher',
                'email': 'stu@gmail.com',
            },
            {
                'username': 'maria',
                'password': 'maria123!',
                'first_name': 'maria',
                'last_name': 'perez',
                'email': 'maria@gmail.com',
            },
            {
                'username': 'carlos',
                'password': 'carlos123!',
                'first_name': 'carlos',
                'last_name': 'gonzalez',
                'email': 'carlos@gmail.com',
            }
        ]

        for usuario in usuarios:
            if not ModeloUsuarioModificado.objects.filter(username=usuario['username']).exists():
                # Si tiene rol, lo pasamos. Si no, dejamos que Django use el default.
                rol = usuario.get('rol', ModeloUsuarioModificado.Roles.USER)

                ModeloUsuarioModificado.objects.create_user(
                    username=usuario['username'],
                    password=usuario['password'],
                    email=usuario['email'],
                    rol=rol,
                    first_name=usuario.get('first_name', ''), # si no existe, se queda vacio
                    last_name=usuario.get('last_name', '') # si no existe, se queda vacio
                )

                self.stdout.write(self.style.SUCCESS(f"Usuario '{usuario['username']}' creado exitosamente."))
            else:
                self.stdout.write(self.style.WARNING(f"El usuario '{usuario['username']}' ya existe."))
