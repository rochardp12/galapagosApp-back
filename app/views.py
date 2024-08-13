from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,action


class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

    @action(detail=False, methods=['get'], url_name='search_role_user')
    def search_role_user(self, request):
        
        data = Negocio.objects.all()
        data = NegocioSerializer(data, many=True).data
        return Response(data, status=201)
        '''data = {
                "id": 2,
                "name": "nombre",
                "day": "dia",
                "time": "tiempo",
                "performed": "yesss"}
        return Response(data)'''
