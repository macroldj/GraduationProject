from django.contrib.auth import get_user_model

from .models import book
from  rest_framework import serializers

User = get_user_model()


class BookSerializers(serializers.Serializer):
    class Meta:
        model = book
        field ="__all__"
