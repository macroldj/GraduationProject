from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import BookSerializers
from .models import book


class BookPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializers


class BookGetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializers