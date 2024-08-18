from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from django.db.models import Q


'''class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

    @action(detail=False, methods=['get'], url_name='buscar_negocio_isla')
    def buscar_negocio_isla(self, request):
        data = Negocio.objects.all()
        data = NegocioSerializer(data, many=True).data
        return Response(data, status=201)
        data = {
                "id": 2,
                "name": "nombre",
                "day": "dia",
                "time": "tiempo",
                "performed": "yesss"}
        return Response(data)'''

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

class BiodiversidadViewSet(viewsets.ModelViewSet):
    queryset = Biodiversidad.objects.all()
    serializer_class = BiodiversidadSerializer

class FaunaViewSet(viewsets.ModelViewSet):
    queryset = Fauna.objects.all()
    serializer_class = FaunaSerializer

class FloraViewSet(viewsets.ModelViewSet):
    queryset = Flora.objects.all()
    serializer_class = FloraSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    @action(detail=False, methods=['get'], url_path=r'nombre_actividad_isla/(?P<nombre_actividad_isla>[\w\s]+)', url_name='buscar_actividad_isla')
    def buscar_actividad_isla(self, request,nombre_actividad_isla):
            data = Actividad.objects.filter(Q(isla__nombre=nombre_actividad_isla))
            if not data.exists():
                return Response({"error": "Actividades no encontradas"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = ActividadSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class GuiasTuristicosViewSet(viewsets.ModelViewSet):
    queryset = GuiasTuristicos.objects.all()
    serializer_class = GuiasTuristicosSerializer

    @action(detail=False, methods=['get'], url_path=r'nombre_isla/(?P<nombre_isla>[\w\s]+)', url_name='buscar_Guia_isla')
    def buscar_Guia_isla(self, request,nombre_isla):
            data = GuiasTuristicos.objects.filter(Q(isla__nombre=nombre_isla))
            if not data.exists():
                return Response({"error": "Guías Turísticos no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = GuiasTuristicosSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class EcosistemaViewSet(viewsets.ModelViewSet):
    queryset = Ecosistema.objects.all()
    serializer_class = EcosistemaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(detail=False, methods=['get'], url_name='obtener_comentarios')
    def obtener_comentarios(self, request):
            data = Comentario.objects.all()
            if not data.exists():
                return Response({"error": "Comentarios no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = ComentarioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
            
    @action(detail=False, methods=['post'], url_path=r'crear_comentario/')
    def crear_comentario(self, request):        
        id_usuario = request.data['usuario']
        texto =request.data['comentario']
        
        usuario = Usuario.objects.filter(Q(id=id_usuario))
        if not usuario.exists():
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        usuario = usuario.first()

        comentario = Comentario.objects.create(
                    usuario = usuario,
                    comentario=texto,
                )           
        serializado = ComentarioSerializer(comentario).data
        return Response(serializado, status=status.HTTP_201_CREATED)

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer