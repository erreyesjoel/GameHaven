"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include # include para incluir las urls de las apps
from . import views # import del views
from usuarios.forms import AdminPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_template, name='login_template'), # template de login, sera la raiz del sitio
    path('restablecer-password/', auth_views.PasswordResetView.as_view(
        form_class=AdminPasswordResetForm,
        template_name='autenticacion/password_reset_form.html',
        email_template_name='autenticacion/password_reset_email.html',
        subject_template_name='autenticacion/password_reset_subject.txt',
        success_url='/restablecer-password/enviado/',
    ), name='password_reset'),
    path('restablecer-password/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='autenticacion/password_reset_done.html'
    ), name='password_reset_done'),
    path('restablecer-password/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='autenticacion/password_reset_confirm.html',
        success_url='/restablecer-password/completado/',
    ), name='password_reset_confirm'),
    path('restablecer-password/completado/', auth_views.PasswordResetCompleteView.as_view(
        template_name='autenticacion/password_reset_complete.html'
    ), name='password_reset_complete'),
    path("logout/", views.logout_view, name="logout"),
    path('juegos/', include('juegos.urls')), # incluimos las urls de la app juegos, juegos (app) urls (juegos/urls.py)
    path('plataformas/', include('plataformas.urls')), # incluimos las urls de la app plataformas, plataformas (app) urls (plataformas/urls.py)
    path('usuarios/', include('usuarios.urls')), # incluimos las urls de la app usuarios, usuarios (app) urls (usuarios/urls.py)
    path('dashboard/', include('dashboard.urls')),
    path('categorias/', include('categorias.urls')),
    path('ajustes/', include('ajustes.urls')),
]
