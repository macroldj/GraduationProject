from .models import UserProfile, VerifyCode
from  rest_framework import serializers


class UserProfileserializers(serializers.Serializer):
    class Meta:
        model = UserProfile
        fileds = "__all__"


class VerifyCodeSerializers(serializers.Serializer):
    class Meta:
        model = VerifyCode
        fileds = "__all__"
