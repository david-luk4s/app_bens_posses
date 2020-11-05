"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from pessoas.viewsets import PessoasViewSet
from empresas.viewsets import EmpresaViewSets
from bens_posses.viewsets import BensPossesViewSet


router = routers.DefaultRouter()
router.register(r'pessoas', PessoasViewSet, basename='pessoas')
router.register(r'empresas', EmpresaViewSets, basename='empresas')
router.register(r'bens_posses', BensPossesViewSet, basename='bens_posses')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
