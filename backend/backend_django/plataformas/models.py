from django.db import models

# Create your models here.
# clase para la tabla plataformas

class Plataforma(models.Model):
    class Tipos(models.TextChoices):
        PC = 'PC', 'PC'
        PLAYSTATION = 'PLAYSTATION', 'PlayStation'
        XBOX = 'XBOX', 'Xbox'
        NINTENDO = 'NINTENDO', 'Nintendo'

    tipo = models.CharField(
        max_length=20,
        choices=Tipos.choices,
    )

    class Meta:
        db_table = 'plataformas' # nombre de la tabla en la base de datos, lo elegimos nosotros con el class meta