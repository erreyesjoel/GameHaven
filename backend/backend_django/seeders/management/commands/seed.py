from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Ejecuta todos los seeders del proyecto"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Iniciando seeders..."))

        # Orden de ejecución de todos los seeders
        call_command("seed_categorias")
        call_command("seed_plataformas")
        call_command("seed_usuarios")
        call_command("seed_juegos")

        self.stdout.write(self.style.SUCCESS("Seeders ejecutados correctamente"))
