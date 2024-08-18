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
    #katherine tumbaco
    @action(detail=False, methods=['get'], url_path=r'registradas', url_name='obtener_islas')
    def obtener_isla(self, request):
            data = Isla.objects.all()
            if not data.exists():
                return Response({"error": "Islas no encontradas"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = IslaSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path=r'(?P<id_isla>\d+)/actualizar_puntuacion/(?P<puntuacion>\d+)', url_name='actualizar_puntuacion')
    def actualizar_puntuacion(self, request, id_isla, puntuacion):
        data = Isla.objects.filter(id=id_isla)
        if not data.exists():
            return Response({"error": "Isla no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            isla = data.first()
            try:
                puntuacion = int(puntuacion)
            except ValueError:
                return Response({"error": "Puntuación no válida"}, status=status.HTTP_400_BAD_REQUEST)
            
            if puntuacion < 1 or puntuacion > 3:
                return Response({"error": "Puntuación debe ser 1, 2 o 3"}, status=status.HTTP_400_BAD_REQUEST)
            
            if puntuacion == 1:
                isla.calificacion_uno += 1
            elif puntuacion == 2:
                isla.calificacion_dos += 1
            elif puntuacion == 3:
                isla.calificacion_tres += 1
            
            isla.save()
            
            return Response({"mensaje": "Puntuación actualizada correctamente"}, status=status.HTTP_200_OK)

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

class GuiasTuristicosViewSet(viewsets.ModelViewSet):
    queryset = GuiasTuristicos.objects.all()
    serializer_class = GuiasTuristicosSerializer

class EcosistemaViewSet(viewsets.ModelViewSet):
    queryset = Ecosistema.objects.all()
    serializer_class = EcosistemaSerializer
    #katherine tumbaco
    @action(detail=False, methods=['get'], url_path=r'registrados', url_name='obtener_ecosistemas')
    def obtener_ecosistemas(self, request,):
            data = Ecosistema.objects.all()
            if not data.exists():
                return Response({"error": "Ecosistemas no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = EcosistemaSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    #katherine tumbaco
    @action(detail=False, methods=['get'], url_path=r'usuario/(?P<id_usuario>\w+)/isla/(?P<id_isla>\w+)', url_name='obtener_celificacion_usuario')
    def obtener_calificacion_usuario(self, request,id_usuario,id_isla):
            data = Calificacion.objects.filter(usuario_id=id_usuario, isla_id=id_isla)
            if not data.exists():
                return Response({"error": "Calificacion no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = CalificacionSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
               
    @action(detail=False, methods=['post'], url_path=r'registrar_calificacion')
    def registrar_calificacion(self, request):        
        voto = request.data['voto']
        puntuacion =  request.data['puntuacion']
        id_isla = request.data['isla']
        id_usuario = request.data['usuario']
       
        
        isla = Isla.objects.filter(Q(id=id_isla))
        if not isla.exists():
            return Response({"error": "Isla no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        usuario = Usuario.objects.filter(Q(id=id_usuario))
        if not usuario.exists():
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        isla = isla.first()
        usuario = usuario.first()

        try:
            puntuacion = int(puntuacion)
        except ValueError:
            return Response({"error": "Puntuación no válida"}, status=status.HTTP_400_BAD_REQUEST)
            
        if puntuacion < 1 or puntuacion > 3:
            return Response({"error": "Puntuación debe ser 1, 2 o 3"}, status=status.HTTP_400_BAD_REQUEST)
            
        if puntuacion == 1:
            isla.calificacion_uno += 1
        elif puntuacion == 2:
            isla.calificacion_dos += 1
        elif puntuacion == 3:
            isla.calificacion_tres += 1
            
        isla.save()

        calificacion = Calificacion.objects.create(
                    voto=voto,
                    puntuacion=puntuacion,
                    usuario = usuario,
                    isla = isla
                )      
            
        serializado = CalificacionSerializer(calificacion).data
        return Response(serializado, status=status.HTTP_201_CREATED)
