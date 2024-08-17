from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from django.db.models import Q

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class IslaViewSet(viewsets.ModelViewSet):
    queryset = Isla.objects.all()
    serializer_class = IslaSerializer

class TipoNegocioViewSet(viewsets.ModelViewSet):
    queryset = TipoNegocio.objects.all()
    serializer_class = TipoNegocioSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

    @action(detail=False, methods=['get'], url_path=r'nombre_isla/(?P<nombre_isla>\w+)', url_name='buscar_negocio_isla')
    def buscar_negocio_isla(self, request,nombre_isla):
            data = Negocio.objects.filter(Q(isla__nombre=nombre_isla))
            if not data.exists():
                return Response({"error": "Negocios no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = NegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path=r'nombre_tipo/(?P<nombre_tipo>\w+)', url_name='buscar_negocio_tipo')
    def buscar_negocio_tipo(self, request,nombre_tipo):
            data = Negocio.objects.filter(Q(tipo_negocio__tipo=nombre_tipo))
            if not data.exists():
                return Response({"error": "Negocios no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = NegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

    @action(detail=False, methods=['post'], url_path=r'crear_resena/')
    def crear_resena(self, request):        
        id_negocio=request.data['negocio']
        id_usuario = request.data['usuario']
        texto=request.data['descripcion']
        
        negocio = Negocio.objects.filter(Q(id=id_negocio))
        if not negocio.exists():
            return Response({"error": "Negocio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        usuario = Usuario.objects.filter(Q(id=id_usuario))
        if not usuario.exists():
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        negocio = negocio.first()
        usuario = usuario.first()

        resena = Resena.objects.create(
                    negocio=negocio,
                    usuario = usuario,
                    descripcion=texto,
                )           
        serializado = ResenaSerializer(resena).data
        return Response(serializado, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'], url_path=r'id_negocio/(?P<id_negocio>\d+)', url_name='buscar_resenas')
    def buscar_resenas(self, request,id_negocio):
            data = Resena.objects.filter(Q(negocio__id=id_negocio))
            if not data.exists():
                return Response({"mensaje": "Sin reseñas"}, status=status.HTTP_200_OK)
            else:
                data = ResenaSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class BiodiversidadViewSet(viewsets.ModelViewSet):
    queryset = Biodiversidad.objects.all()
    serializer_class = BiodiversidadSerializer

class FaunaViewSet(viewsets.ModelViewSet):
    queryset = Fauna.objects.all()
    serializer_class = FaunaSerializer

    @action(detail=False, methods=['get'], url_name='buscar_fauna')
    def buscar_fauna(self, request):
            data = Fauna.objects.all()
            if not data.exists():
                return Response({"error": "Sin fauna registrada"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = FaunaSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class FloraViewSet(viewsets.ModelViewSet):
    queryset = Flora.objects.all()
    serializer_class = FloraSerializer

    @action(detail=False, methods=['get'], url_name='buscar_flora')
    def buscar_flora(self, request):
            data = Flora.objects.all()
            if not data.exists():
                return Response({"error": "Sin flora registrada"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = FloraSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class GuiasTuristicosViewSet(viewsets.ModelViewSet):
    queryset = GuiasTuristicos.objects.all()
    serializer_class = GuiasTuristicosSerializer

class EcosistemaViewSet(viewsets.ModelViewSet):
    queryset = Ecosistema.objects.all()
    serializer_class = EcosistemaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer