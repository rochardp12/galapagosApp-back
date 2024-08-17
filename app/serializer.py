from rest_framework import serializers
from app.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nickname']

class UsuarioPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class IslaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isla
        fields = "__all__"

class TipoNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNegocio
        fields = "__all__"

class NegocioSerializer(serializers.ModelSerializer):
    tipo_negocio = TipoNegocioSerializer(many=False, read_only=True)
    isla = IslaSerializer(many=False, read_only=True)
    class Meta:
        model = Negocio
        fields = "__all__"

class ResenaSerializer(serializers.ModelSerializer):
    negocio = NegocioSerializer(many=False, read_only=True)
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Resena
        fields = "__all__"

class BiodiversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodiversidad
        fields = "__all__"

class FaunaSerializer(BiodiversidadSerializer):
    class Meta:
        model = Fauna
        fields = "__all__"

class FloraSerializer(BiodiversidadSerializer):
    class Meta:
        model = Flora
        fields = "__all__"

class ActividadSerializer(serializers.ModelSerializer):
    isla = IslaSerializer(many=False, read_only=True)
    class Meta:
        model = Actividad
        fields = "__all__"

class GuiasTuristicosSerializer(serializers.ModelSerializer):
    isla = IslaSerializer(many=False, read_only=True)
    class Meta:
        model = GuiasTuristicos
        fields = "__all__"

class EcosistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecosistema
        fields = "__all__"

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Comentario
        fields = "__all__"

class CalificacionSerializer(serializers.ModelSerializer):
    isla = IslaSerializer(many=False, read_only=True)
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Calificacion
        fields = "__all__"