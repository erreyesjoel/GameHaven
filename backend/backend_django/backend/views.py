from django.shortcuts import render # importante para renderizar plantillas como html

def ejemplo_template(request):
    return render(request, 'template_principal_ejemplo.html')

# def para renderizar el template de login
def login_template(request):
    return render(request, 'autenticacion/login.html')