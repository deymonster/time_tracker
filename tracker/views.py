from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ClientSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

