"""
URL configuration for galapagosApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from app import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'isla', views.IslaViewSet)
router.register(r'tipo_negocio', views.TipoNegocioViewSet)
router.register(r'negocio', views.NegocioViewSet)
router.register(r'resena', views.ResenaViewSet)
router.register(r'biodiversidad', views.BiodiversidadViewSet)
router.register(r'fauna', views.FaunaViewSet)
router.register(r'flora', views.FloraViewSet)
router.register(r'actividad', views.ActividadViewSet)
router.register(r'guias_turisticos', views.GuiasTuristicosViewSet)
router.register(r'ecosistema', views.EcosistemaViewSet)
router.register(r'comentario', views.ComentarioViewSet)
router.register(r'calificacion', views.CalificacionViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Galapagos API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include(router.urls)),
]
