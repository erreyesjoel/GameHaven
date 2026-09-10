# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required

# Create your views here.
# def para mostrar la pagina de ajustes
# pyrefly: ignore [missing-signature]
@login_required
def mostrar_ajustes(request):
    return render(request, 'admin/ajustes.html', {'active_page': 'ajustes'})