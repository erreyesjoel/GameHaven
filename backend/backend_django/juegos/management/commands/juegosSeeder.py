from django.core.management.base import BaseCommand
from juegos.models import Juego, Juegos_Plataformas, Fotos_Juegos
from categorias.models import Categoria
from plataformas.models import Plataforma

class Command(BaseCommand):
    help = 'Crea 12 juegos de ejemplo con plataformas y fotos'

    def handle(self, *args, **options):
        # Diccionario de plataformas por nombre para fácil acceso
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
                    "https://static.bandainamcoent.eu/high/dragon-ball/dragon-ball-sparking-zero/00-page-setup/dbsz_keyart.jpg"
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
                    "https://static.bandainamcoent.eu/high/dragon-ball/dragon-ball-xenoverse-2/00-page-setup/dbxv2_keyart.jpg"
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
                    "https://static.bandainamcoent.eu/high/naruto/naruto-shippuden-ultimate-ninja-storm-4/00-page-setup/naruto_keyart.jpg"
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
                    "https://media.contentapi.ea.com/content/dam/ea/fc/fc-24/common/fc24-keyart.jpg"
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
                    "https://zelda.nintendo.com/breath-of-the-wild/assets/media/header/Main-Day.jpg"
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
                    "https://www.minecraft.net/content/dam/games/minecraft/key-art/Minecraft-xbox-keyart.jpg"
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
                    "https://media-rockstargames-com.akamaized.net/tina-uploads/posts/9k2k4k9o3k2k4k9o3k2k/gtav-keyart.jpg"
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
                    "https://compass-ssl.xbox.com/assets/2d/6b/2d6b2b2d-1b1b-4b4b-8b8b-2b2b2b2b2b2b.jpg"
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
                    "https://www.animal-crossing.com/new-horizons/assets/img/global/header/acnh-keyart.jpg"
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
                    "https://cdn.cdprojektred.com/thewitcher.com/media/w3_keyart_1920x1080.jpg"
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
                    "https://www.nintendo.com/content/dam/noa/en_US/games/switch/s/super-mario-odyssey-switch/super-mario-odyssey-switch-hero.jpg"
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
                    "https://www.callofduty.com/content/dam/atvi/callofduty/cod-touchui/mw2/home/keyart/MWII-REVEAL-TOUT.jpg"
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

            # Añadir fotos
            for url in juego_data["fotos"]:
                Fotos_Juegos.objects.get_or_create(juego=juego, url=url)

