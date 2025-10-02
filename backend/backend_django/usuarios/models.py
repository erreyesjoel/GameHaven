from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# enum, choices, choices es como enums en otros lenguajes
# AbstractUser es el modelo por defecto de django para usuarios
class ModeloUsuarioModificado(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        USER = 'USER', 'Usuario'

    rol = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER
    )

    class Meta:
        db_table = 'usuarios'  # nombre de la tabla en la base de datos