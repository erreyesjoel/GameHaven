from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

class Command(BaseCommand):
    help = "Reinicia la base de datos, migra y ejecuta los seeders (tipo migrate:fresh --seed)"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Eliminando todas las tablas de PostgreSQL..."))

        with connection.cursor() as cursor:
            cursor.execute("""
                DO $$ DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                    END LOOP;
                END $$;
            """)

        self.stdout.write(self.style.SUCCESS("Todas las tablas eliminadas."))

        # Migrar de nuevo
        self.stdout.write(self.style.WARNING("Ejecutando migraciones..."))
        call_command("migrate")

        # Ejecutar seeders
        self.stdout.write(self.style.WARNING("Ejecutando seeders..."))
        call_command("seed")

        self.stdout.write(self.style.SUCCESS("Base de datos reiniciada y seeders ejecutados correctamente."))
