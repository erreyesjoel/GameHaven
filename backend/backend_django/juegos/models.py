from django.db import models
# importamos la app categorias con el from, y con el import la clase Categoria
from categorias.models import Categoria
# importamos la app plataformas con el from, y con el import la clase Plataforma
from plataformas.models import Plataforma

# Create your models here.
# clase para la tabla juegos
class Juego(models.Model):
    PEGI_CHOICES = [
        (3, 'PEGI 3'),
        (7, 'PEGI 7'),
        (12, 'PEGI 12'),
        (16, 'PEGI 16'),
        (18, 'PEGI 18'),
    ]
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    fecha_lanzamiento = models.DateField()
    pegi = models.IntegerField(choices=PEGI_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Categoria es la clase que importamos de categorias.models, el class Categoria

    class Meta:
        db_table = 'juegos' # nombre de la tabla en la base de datos, lo elegimos nosotros con el class meta

# clase para tabla pivote, relacion muchos a muchos N:M entre juegos y plataformas
class Juegos_Plataformas(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE) # Juego es la clase que importamos de juegos.models, el class Juego
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE) # Plataforma es la clase que importamos de plataformas.models, el class Plataforma

    class Meta:
        db_table = 'juegos_plataformas' # nombre de la tabla en la base de datos, lo elegimos nosotros con el class meta
        unique_together = ('juego', 'plataforma') # para que no se repitan los pares juego-plataforma en la tabla pivote, es decir, que un juego no pueda estar dos veces en la misma plataforma