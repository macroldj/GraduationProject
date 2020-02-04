from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .models import ShoppingCart, OrderGoods, OrderInfo
from .serializers import ShoppingCartSerializers,OrderGoodsSerializers,OrderInfoSerializers


class ShoppingCartViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车
    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers


class OrderGoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车货物
    """
    queryset = OrderGoods.objects.all()
    serializer_class = ShoppingCartSerializers


class OrderInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车信息
    """
    queryset = OrderInfo.objects.all()
    serializer_class = ShoppingCartSerializers