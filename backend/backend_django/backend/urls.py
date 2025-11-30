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
from django.urls import path, include # include para incluir las urls de las apps
from . import views # import del views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_template, name='login_template'), # template de login, sera la raiz del sitio
    path('dashboard', views.admin_dashboard_template, name='admin_dashboard_template'), # template del dashboard de admin, http://127.0.0.1:8002/dashboard
    path("logout/", views.logout_view, name="logout"),
    path('juegos/', include('juegos.urls')), # incluimos las urls de la app juegos, juegos (app) urls (juegos/urls.py)
]
