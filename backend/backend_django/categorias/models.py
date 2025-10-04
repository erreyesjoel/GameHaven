from django.db import models

# Create your models here.
# clase para la tabla categorias

class Categoria(models.Model):
    class Categorias(models.TextChoices):
        DEPORTES = 'DEPORTES', 'Deportes'
        LUCHAS = 'LUCHAS', 'Luchas'
        CARRERAS = 'CARRERAS', 'Carreras'
        ACCION = 'ACCION', 'Acción'
        AVENTURAS = 'AVENTURAS', 'Aventuras'
        RPG = 'RPG', 'Rol (RPG)'
        ESTRATEGIA = 'ESTRATEGIA', 'Estrategia'
        SIMULACION = 'SIMULACION', 'Simulación'
        PUZZLE = 'PUZZLE', 'Puzzle'
        TERROR = 'TERROR', 'Terror'
        SHOOTER = 'SHOOTER', 'Shooter'
        PLATAFORMAS = 'PLATAFORMAS', 'Plataformas'
        MUSICAL = 'MUSICAL', 'Musical'
        PARTY = 'PARTY', 'Party'
        SANDBOX = 'SANDBOX', 'Sandbox'
        MMO = 'MMO', 'MMO'
        EDUCATIVO = 'EDUCATIVO', 'Educativo'
        OTROS = 'OTROS', 'Otros'

    nombre_categoria = models.CharField(
        max_length=30,
        choices=Categorias.choices,
        unique=True
    )

    class Meta:
        db_table = 'categorias' # nombre de la tabla en la base de datos, lo elegimos nosotros con el class meta
