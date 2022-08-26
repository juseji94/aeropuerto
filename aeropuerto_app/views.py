from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets,status
# Create your views here.

class Avion_view(viewsets.ModelViewSet):
    #queryset = Avion.objects.all().order_by('-codigo_avion')
    queryset = Avion.objects.all()
    serializer_class = Avion_Serializer
