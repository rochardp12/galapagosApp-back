from rest_framework import serializers
from app.models import *

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
    class Meta:
        model = Resena
        fields = "__all__"