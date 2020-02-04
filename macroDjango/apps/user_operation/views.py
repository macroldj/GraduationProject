from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from .models import UserAddress, UserFav, UserLeavingMessage, User
from .serializers import UserSerializers,UserFavSerializers,UserAddressSerializers,UserLeavingMessageSerializers

# Create your views here.


class UserViewSets(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    用户展示
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserFavViewSets(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    用户收藏
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializers


class UserLeavingMessageViewSets(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    用户留言信息
    """
    queryset = UserLeavingMessage.objects.all()
    serializer_class = UserLeavingMessageSerializers


class UserAddressViewSets(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    用户地址信息
    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializers