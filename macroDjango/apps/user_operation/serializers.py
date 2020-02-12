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
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True , format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = (
        "id" , "user" , "province" , "city" , "district" , "address" , "signer_name" , "add_time" , "signer_mobile")


class UserLeavingMessageSerializers(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject  ", "message", "file", "id" ,"add_time")


class UserSerializers(serializers.Serializer):
    class Meta:
        model = User
        filed = "__all__"