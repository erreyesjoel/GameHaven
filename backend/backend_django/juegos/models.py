from django.db import models
# importamos la app categorias con el from, y con el import la clase Categoria
from categorias.models import Categoria

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
