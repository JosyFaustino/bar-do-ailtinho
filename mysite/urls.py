"""
    Este script faz o controle do funcionamento das urls do site

    
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # administração do django
    path('admin/', admin.site.urls),
    # autenticação de usuários
    path('accounts/', include('allauth.urls')),
    path("", include("pages.urls", namespace="pages")),
    # aplicativo da cozinha
    path('cozinha/', include('cozinha.urls')),  
    # aplicativo dos clientes    # o método include() busca n
    path('clientes/', include('clientes.urls')),
]