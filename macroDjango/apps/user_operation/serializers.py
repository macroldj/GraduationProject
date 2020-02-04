from rest_framework import serializers
from .models import UserAddress, UserFav, UserLeavingMessage, User


class UserFavSerializers(serializers.Serializer):
    class Meta:
        model = UserFav
        filed = "__all__"


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