from django.core.management.base import BaseCommand  # Importa la clase base para comandos personalizados de Django
from plataformas.models import Plataforma  # Importa el modelo de plataformas

class Command(BaseCommand):
    help = 'Crea todas las plataformas definidas en los choices de Plataforma'  # Descripción del comando, aparece con --help

    def handle(self, *args, **options):
        for key, label in Plataforma.Tipos.choices:
            obj, created = Plataforma.objects.get_or_create(tipo=key)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Plataforma '{label}' creada."))
            else:
                self.stdout.write(self.style.WARNING(f"Plataforma '{label}' ya existe."))