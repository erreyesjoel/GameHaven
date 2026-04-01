from usuarios.models import ModeloUsuarioModificado
from juegos.models import Juego
from plataformas.models import Plataforma
from categorias.models import Categoria

def mostrar_datos_dashboard():
    return {
        'total_usuarios': ModeloUsuarioModificado.objects.count(),
        'total_juegos': Juego.objects.count(),
        'total_plataformas': Plataforma.objects.count(),
        'total_categorias': Categoria.objects.count(),
    }