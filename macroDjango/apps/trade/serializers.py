from rest_framework import serializers

from .models import ShoppingCart, OrderGoods, OrderInfo


class ShoppingCartSerializers(serializers.Serializer):
    class Meta:
        model = ShoppingCart
        fileds = "__all__"


class OrderGoodsSerializers():
    class Meta:
        model = OrderGoods
        fileds = "__all__"


class OrderInfoSerializers():
    class Meta:
        model = OrderInfo
        fileds = "__all__"
