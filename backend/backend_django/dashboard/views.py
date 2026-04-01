from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import ModeloUsuarioModificado

@login_required(login_url='/')
def admin_dashboard(request):
    return render(request, 'admin/dashboardAdmin.html', {
        'active_page': 'dashboard'
    })
