from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serializers import GoodsSerializers
from .models import UserAddress, UserFav, UserLeavingMessage, User


class UserFavDetailSerializers(serializers.Serializer):
    goods = GoodsSerializers()

    class Meta:
        model = UserFav
        fields = ("goods" , "id")


class UserFavSerializers(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")


class UserAddressSerializers(serializers.Serializer):
    class Meta:
        model = UserAddress
        filed = "__all__"


class UserLeavingMessageSerializers(serializers.Serializer):
    class Meta:
        model = UserLeavingMessage
        filed = "__all__"


class UserSerializers(serializers.Serializer):
    class Meta:
        model = User
        filed = "__all__"