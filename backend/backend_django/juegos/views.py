from django.shortcuts import render, redirect, get_object_or_404 # importamos render para renderizar templates y redirect para redirigir, get_object_or_404 para obtener objetos o devolver 404
from juegos.models import Juego # importamos el modelo
from plataformas.models import Plataforma # importamos el modelo
from django.contrib.auth.decorators import login_required # para proteger las vistas

# Create your views here.
# renderizar juegos.html y funcion para devolver los juegos
@login_required
def mostrarJuegos(request):
    juegos = Juego.objects.all() # obtenemos todos los juegos
    plataformas = Plataforma.objects.all() # obtenemos todas las plataformas
    return render(request, 'admin/juegos.html', {'juegos': juegos, 'plataformas': plataformas})

@login_required
# funcion (def) para eliminar un juego 
def eliminarJuego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id) # obtenemos el juego por su id
    juego.delete() # eliminamos el juego
    return redirect('mostrar_juegos') # redirigimos a la lista de juegos

@login_required
# def para editar juego
def editarJuego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id) # buscamos juego por id
    if request.method == 'POST':
        # obtenemos todos los datos del juego
        juego.titulo = request.POST.get('titulo', juego.titulo)
        juego.descripcion = request.POST.get('descripcion', juego.descripcion)
        juego.precio = request.POST.get('precio', juego.precio)
        juego.stock = request.POST.get('stock', juego.stock)
        juego.fecha_lanzamiento = request.POST.get('fecha_lanzamiento', juego.fecha_lanzamiento)
        juego.pegi = request.POST.get('pegi', juego.pegi)
        categoria_id = request.POST.get('categoria')
        foto_juego_url = request.POST.get('foto_juego_url') # obtenemos la url de la foto del juego
        if categoria_id:
            from categorias.models import Categoria
            juego.categoria = get_object_or_404(Categoria, id=categoria_id)
        # actualizar la foto del juego si se ha enviado una nueva url
        if foto_juego_url:
            foto = juego.fotos_juegos_set.first() # obtenemos la primera foto relacionada
            if foto:
                foto.url = foto_juego_url # actualizamos la url
                foto.save() # guardamos la foto
            else:
                from juegos.models import Fotos_Juegos
                Fotos_Juegos.objects.create(juego=juego, url=foto_juego_url) # creamos la foto si no existe
        juego.save() # guardamos los cambios
        return redirect('mostrar_juegos') # redirigimos a la lista de juegos
    return render(request, 'admin/editarJuego.html', {'juego': juego}) # renderizamos el template de editar juego