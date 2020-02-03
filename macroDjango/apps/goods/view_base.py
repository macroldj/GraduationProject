__auther__ = 'macroldj'

from django.views.generic.base import View
from .models import Goods

from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict

from django.core import serializers

import json

class GoodsListView(View):
    def get(self,request):
        """
        展示列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)
