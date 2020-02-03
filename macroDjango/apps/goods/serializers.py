from rest_framework import serializers

from goods.models import Goods, GoodsCategory, GoodsImage, HotSearchWords, Banner, GoodsCategoryBrand


class GoodsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializers(serializers.ModelSerializer):
    category = GoodsCategorySerializers()
    class Meta:
        model = Goods
        fields = "__all__"