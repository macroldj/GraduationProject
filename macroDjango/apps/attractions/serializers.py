from django.contrib.auth import get_user_model

from .models import Attractions
from  rest_framework import serializers

User = get_user_model()


class AttractionsSerializers(serializers.ModelSerializer):
    name = serializers.CharField(label="name", help_text="景点", max_length=20)
    auther = serializers.CharField(label="auther", help_text="城市", max_length=20)
    mobile = serializers.CharField(label="mobile", help_text="手机号码", max_length=11)

    class Meta:
        model = Attractions
        fields = ("name", "auther", "mobile")
