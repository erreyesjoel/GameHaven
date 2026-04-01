from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import mostrar_datos_dashboard

@login_required(login_url='/')
def admin_dashboard(request):
    datos = mostrar_datos_dashboard()
    return render(request, 'admin/dashboardAdmin.html', {
        'active_page': 'dashboard',
        'datos': datos
    })

