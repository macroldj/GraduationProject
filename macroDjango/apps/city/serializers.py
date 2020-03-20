from django.contrib.auth import get_user_model

from .models import city
from  rest_framework import serializers

User = get_user_model()


class CitySerializers(serializers.ModelSerializer):
    name = serializers.CharField(label="name", help_text="城市名", max_length=20)
    auther = serializers.CharField(label="address", help_text="地址", max_length=20)
    mobile = serializers.CharField(label="mobile", help_text="联系号码", max_length=11)

    class Meta:
        model = city
        fields = ("name", "auther", "mobile")
