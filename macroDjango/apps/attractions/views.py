from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import AttractionsSerializers
from .models import Attractions


class AttractionsPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializers


class AttractionsGetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializers