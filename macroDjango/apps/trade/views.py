from datetime import datetime

from django.shortcuts import render , redirect
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from .wxPay import WechatPaymentXMLParser , WechatPayXMLRender
from .models import ShoppingCart, OrderGoods, OrderInfo
from .serializers import ShoppingCartSerializers,OrderGoodsSerializers,OrderInfoSerializers


class ShoppingCartViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车
    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers


class OrderGoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车货物
    """
    queryset = OrderGoods.objects.all()
    serializer_class = ShoppingCartSerializers


class OrderInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    购物车信息
    """
    queryset = OrderInfo.objects.all()
    serializer_class = ShoppingCartSerializers


from rest_framework.views import APIView
from utils.alipay import AliPay
from macroDjango.settings import ali_pub_key_path, private_key_path
from rest_framework.response import Response


class AlipayView(APIView):
    def get(self, request):
        """
        处理支付宝的return_url返回
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', None)

            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            response = redirect("index")
            response.set_cookie("nextPath","pay", max_age=3)
            return response
        else:
            response = redirect("index")
            return response

    def post(self, request):
        """
        处理支付宝的notify_url
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', None)

            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                order_goods = existed_order.goods.all()
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            return Response("success")


class WeChatNotifyPayView(APIView):
    """
    微信支付回调接口
    """
    authentication_classes = []
    permission_classes = (AllowAny,)
    parser_classes = (WechatPaymentXMLParser, )
    renderer_classes = (WechatPayXMLRender, )
    # serializer_class = PayRecordSerializer
    #
    # def initialize_request(self, request, *args, **kwargs):
    #     """
    #     Returns the initial request object.
    #     """
    #     parser_context = self.get_parser_context(request)
    #
    #     return Request(
    #         request,
    #         parsers=self.get_parsers(),
    #         authenticators=self.get_authenticators(),
    #         negotiator=self.get_content_negotiator(),
    #         parser_context=parser_context
    #     )
    pass