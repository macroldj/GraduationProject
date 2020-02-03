from .serializers import GoodsSerializers
from .models import Goods

from rest_framework import generics


class GoodsList(generics.ListAPIView):
    queryset = Goods.objects.all()[:20]
    serializer_class = GoodsSerializers

