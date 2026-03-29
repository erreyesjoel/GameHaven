from django.core.management.base import BaseCommand
from categorias.models import Categoria

class Command(BaseCommand):
    help = 'Crea todas las categorías definidas en los choices de Categoria'

    def handle(self, *args, **options):
        for key, label in Categoria.Categorias.choices:
            obj, created = Categoria.objects.get_or_create(nombre_categoria=key)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Categoría '{label}' creada."))
            else:
                self.stdout.write(self.style.WARNING(f"Categoría '{label}' ya existe."))