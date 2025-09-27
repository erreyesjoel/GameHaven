from django.shortcuts import render # importante para renderizar plantillas como html

# def para renderizar el template de login
def login_template(request):
    return render(request, 'autenticacion/login.html')

# def para renderiz el dashboard de admin al logearnos en django admin (template)
def admin_dashboard_template(request):
    return render(request, 'admin/dashboardAdmin.html')
    