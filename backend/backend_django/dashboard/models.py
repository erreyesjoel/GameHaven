from django.db import models
from usuarios.models import ModeloUsuarioModificado


# Enum de acciones permitidas para mantener consistencia en filtros, CSV y auditoría
class AccionAuditoria(models.TextChoices):
    LOGIN = "LOGIN", "Inicio de sesión"
    LOGOUT = "LOGOUT", "Cierre de sesión"
    USUARIO_CREADO = "USUARIO_CREADO", "Usuario creado"
    JUEGO_EDITADO = "JUEGO_EDITADO", "Juego editado"
    PLATAFORMA_ELIMINADA = "PLATAFORMA_ELIMINADA", "Plataforma eliminada"
    CATEGORIA_CAMBIADA = "CATEGORIA_CAMBIADA", "Categoría cambiada"
    CORREO_ENVIADO = "CORREO_ENVIADO", "Correo enviado"


# Modelo de actividad-auditoria para registrar acciones relevantes en el panel
# Tabla actividades_auditoria 1:N con usuarios, ya que un usuario puede realizar muchas acciones, pero cada acción pertenece a un solo usuario.
class ActividadAuditoria(models.Model):
    # Usamos SET_NULL en lugar de CASCADE: si en algún momento eliminas a un usuario desde el panel,
    # con CASCADE se borrarían todos sus registros de auditoría y perderías el historial de lo que hizo;
    # con SET_NULL el registro se mantiene intacto.
    usuario = models.ForeignKey(
        'usuarios.ModeloUsuarioModificado',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Usamos TextChoices para evitar textos inconsistentes al filtrar o exportar;
    # el detalle concreto del objeto afectado se guarda en el campo `detalle`.
    accion = models.CharField(
        max_length=50,
        choices=AccionAuditoria.choices,
    )
    detalle = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'actividades_auditoria'
        verbose_name = 'Actividad de auditoría'
        verbose_name_plural = 'Actividades de auditoría'
        ordering = ['-fecha_hora']

    def __str__(self):
        # Validación en __str__: al permitir null=True en usuario (o si algún evento ocurre sin
        # sesión activa, como un intento fallido), self.usuario.username lanzaría un AttributeError
        # si usuario es None; con el fallback 'Usuario eliminado' queda blindado.
        username = self.usuario.username if self.usuario else 'Usuario eliminado'
        return f"{username} - {self.get_accion_display()} - {self.fecha_hora}"