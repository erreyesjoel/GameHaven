from django.core.management.base import BaseCommand
from juegos.models import Juego, Juegos_Plataformas, Fotos_Juegos
from categorias.models import Categoria
from plataformas.models import Plataforma

class Command(BaseCommand):
    help = 'Crea 12 juegos de ejemplo con plataformas y fotos'

    def handle(self, *args, **options):
        plataformas = {p.tipo: p for p in Plataforma.objects.all()}
        categorias = {c.nombre_categoria: c for c in Categoria.objects.all()}

        juegos_data = [
            {
                "titulo": "Dragon Ball Sparking Zero",
                "descripcion": "El nuevo juego de lucha de Dragon Ball para nueva generación.",
                "precio": 69.99,
                "stock": 20,
                "fecha_lanzamiento": "2024-10-01",
                "pegi": 12,
                "categoria": categorias.get("LUCHAS"),
                "plataformas": ["PLAYSTATION"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/231/231233.png"  # Dragon Ball Sparking Zero portada GAME
                ]
            },
            {
                "titulo": "Dragon Ball Xenoverse 2",
                "descripcion": "Continúa la historia de los patrulleros del tiempo.",
                "precio": 39.99,
                "stock": 15,
                "fecha_lanzamiento": "2016-10-28",
                "pegi": 12,
                "categoria": categorias.get("LUCHAS"),
                "plataformas": ["PLAYSTATION"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/143/143365.png"  # Dragon Ball Xenoverse 2 portada GAME
                ]
            },
            {
                "titulo": "Naruto Shippuden: Ultimate Ninja Storm 4",
                "descripcion": "El combate ninja definitivo.",
                "precio": 29.99,
                "stock": 10,
                "fecha_lanzamiento": "2016-02-05",
                "pegi": 12,
                "categoria": categorias.get("LUCHAS"),
                "plataformas": ["PLAYSTATION", "PC"],
                "fotos": [
                    "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/349040/header.jpg?t=1703080866"  # Naruto Storm 4 portada GAME
                ]
            },
            {
                "titulo": "EA Sports FC 26",
                "descripcion": "El simulador de fútbol más realista.",
                "precio": 69.99,
                "stock": 30,
                "fecha_lanzamiento": "2025-09-20",
                "pegi": 3,
                "categoria": categorias.get("DEPORTES"),
                "plataformas": ["PLAYSTATION", "PC", "XBOX"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/230/230123.png"  # EA Sports FC 24 portada GAME (no existe FC 26 aún)
                ]
            },
            {
                "titulo": "The Legend of Zelda: Breath of the Wild",
                "descripcion": "Una aventura épica en Hyrule.",
                "precio": 59.99,
                "stock": 12,
                "fecha_lanzamiento": "2017-03-03",
                "pegi": 12,
                "categoria": categorias.get("AVENTURAS"),
                "plataformas": ["NINTENDO"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/140/140634.png"  # Zelda Breath of the Wild portada GAME
                ]
            },
            {
                "titulo": "Minecraft",
                "descripcion": "Construye y explora mundos infinitos.",
                "precio": 26.95,
                "stock": 50,
                "fecha_lanzamiento": "2011-11-18",
                "pegi": 7,
                "categoria": categorias.get("SANDBOX"),
                "plataformas": ["PC", "PLAYSTATION", "XBOX", "NINTENDO"],
                "fotos": [
                    "https://gaming-cdn.com/images/products/442/616x353/minecraft-java-bedrock-edition-java-bedrock-edition-pc-juego-cover.jpg?v=1716387513"  # Minecraft Switch portada GAME
                ]
            },
            {
                "titulo": "Grand Theft Auto V",
                "descripcion": "Acción y crimen en Los Santos.",
                "precio": 29.99,
                "stock": 25,
                "fecha_lanzamiento": "2013-09-17",
                "pegi": 18,
                "categoria": categorias.get("ACCION"),
                "plataformas": ["PC", "PLAYSTATION", "XBOX"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/123/123936.png"  # GTA V portada GAME
                ]
            },
            {
                "titulo": "Forza Horizon 5",
                "descripcion": "Carreras en mundo abierto en México.",
                "precio": 59.99,
                "stock": 18,
                "fecha_lanzamiento": "2021-11-09",
                "pegi": 3,
                "categoria": categorias.get("CARRERAS"),
                "plataformas": ["PC", "XBOX"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/222/222530.png"  # Forza Horizon 5 portada GAME
                ]
            },
            {
                "titulo": "Animal Crossing: New Horizons",
                "descripcion": "Crea tu isla y haz nuevos amigos.",
                "precio": 49.99,
                "stock": 20,
                "fecha_lanzamiento": "2020-03-20",
                "pegi": 3,
                "categoria": categorias.get("SIMULACION"),
                "plataformas": ["NINTENDO"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/163/163296.png"  # Animal Crossing portada GAME
                ]
            },
            {
                "titulo": "The Witcher 3: Wild Hunt",
                "descripcion": "Una aventura de rol épica.",
                "precio": 39.99,
                "stock": 14,
                "fecha_lanzamiento": "2015-05-19",
                "pegi": 18,
                "categoria": categorias.get("RPG"),
                "plataformas": ["PC", "PLAYSTATION", "XBOX", "NINTENDO"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/140/140636.png"  # The Witcher 3 portada GAME
                ]
            },
            {
                "titulo": "Super Mario Odyssey",
                "descripcion": "La gran aventura de Mario en 3D.",
                "precio": 59.99,
                "stock": 16,
                "fecha_lanzamiento": "2017-10-27",
                "pegi": 7,
                "categoria": categorias.get("PLATAFORMAS"),
                "plataformas": ["NINTENDO"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/144/144861.png"  # Super Mario Odyssey portada GAME
                ]
            },
            {
                "titulo": "Call of Duty: Modern Warfare II",
                "descripcion": "Acción bélica moderna.",
                "precio": 69.99,
                "stock": 22,
                "fecha_lanzamiento": "2022-10-28",
                "pegi": 18,
                "categoria": categorias.get("SHOOTER"),
                "plataformas": ["PC", "PLAYSTATION", "XBOX"],
                "fotos": [
                    "https://media.game.es/COVERV2/3D_L/228/228377.png"  # Call of Duty MWII portada GAME
                ]
            },
        ]

        for juego_data in juegos_data:
            juego, created = Juego.objects.get_or_create(
                titulo=juego_data["titulo"],
                defaults={
                    "descripcion": juego_data["descripcion"],
                    "precio": juego_data["precio"],
                    "stock": juego_data["stock"],
                    "fecha_lanzamiento": juego_data["fecha_lanzamiento"],
                    "pegi": juego_data["pegi"],
                    "categoria": juego_data["categoria"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Juego '{juego.titulo}' creado."))
            else:
                self.stdout.write(self.style.WARNING(f"Juego '{juego.titulo}' ya existe."))

            # Relacionar con plataformas
            for plat in juego_data["plataformas"]:
                plataforma = plataformas.get(plat)
                if plataforma:
                    Juegos_Plataformas.objects.get_or_create(juego=juego, plataforma=plataforma)

            # Eliminar fotos antiguas y añadir las nuevas
            # cada vez que se corre el seeder se actualizan las fotos
            Fotos_Juegos.objects.filter(juego=juego).delete()
            for url in juego_data["fotos"]:
                Fotos_Juegos.objects.create(juego=juego, url=url)
                self.stdout.write(self.style.SUCCESS(f"Foto añadida a '{juego.titulo}': {url}"))

