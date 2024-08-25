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

    @action(detail=False, methods=['post'], url_path=r'crear_usuario/')
    def crear_usuario(self, request):        
        nickname = request.data['nickname']
        password = request.data['password']
        
        creado = Usuario.objects.filter(Q(nickname = nickname))
        if creado.exists():
            return Response({"error": "Nickname ya registrado"}, status=status.HTTP_409_CONFLICT)

        usuario = Usuario.objects.create(
                    nickname = nickname,
                    password = password,
                )           
        serializado = UsuarioSerializer(usuario).data
        return Response(serializado, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path=r'nickname/(?P<nickname>\w+)', url_name='buscar_usuario')
    def buscar_usuario(self, request,nickname):
            data = Usuario.objects.filter(Q(nickname=nickname))
            if not data.exists():
                return Response({"error": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = UsuarioPasswordSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
            
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

    @action(detail=False, methods=['get'], url_name='tipos_negocio')
    def tipos_negocio(self, request):
            data = TipoNegocio.objects.all()
            if not data.exists():
                return Response({"error": "Sin tipos registrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = TipoNegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

    @action(detail=False, methods=['get'], url_path=r'nombre_isla/(?P<nombre_isla>[\w\s]+)', url_name='buscar_negocios_isla')
    def buscar_negocios_isla(self, request,nombre_isla):
            data = Negocio.objects.filter(Q(isla__nombre=nombre_isla))
            if not data.exists():
                return Response({"error": "Negocios no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = NegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path=r'nombre_tipo/(?P<nombre_tipo>\w+)', url_name='buscar_negocios_tipo')
    def buscar_negocios_tipo(self, request,nombre_tipo):
            data = Negocio.objects.filter(Q(tipo_negocio__tipo=nombre_tipo))
            if not data.exists():
                return Response({"error": "Negocios no encontrados"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = NegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
            

    @action(detail=False, methods=['get'], url_path=r'id_negocio/(?P<id_negocio>\d+)', url_name='buscar_negocio_id')
    def buscar_negocios_id(self, request,id_negocio):
            data = Negocio.objects.filter(Q(id=id_negocio))
            if not data.exists():
                return Response({"error": "Negocio no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = NegocioSerializer(data, many=True).data
                return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_name='buscar_negocios')
    def buscar_negocios(self, request):
            data = Negocio.objects.all()
            if not data.exists():
                return Response({"error": "Sin negocios registrados"}, status=status.HTTP_404_NOT_FOUND)
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
                return Response({"error": "Sin reseñas"}, status=status.HTTP_404_NOT_FOUND)
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
