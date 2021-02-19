from django.shortcuts import render
from rest_framework import viewsets
from .models import weather
from .serializers import WeatherSerializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WeatherSerializers
    queryset = weather.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('City',)
