from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import CitySerializers
from .models import city


class BookPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = city.objects.all()
    serializer_class = CitySerializers


class BookGetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = city.objects.all()
    serializer_class = CitySerializers