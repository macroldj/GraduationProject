from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets

from user.models import UserProfile, VerifyCode
from user.serializers import UserProfileserializers, VerifyCodeSerializers


class UserProfileViewsets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileserializers


class VerifyCodeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializers
