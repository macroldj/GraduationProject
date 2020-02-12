from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import ShoppingCartViewSet , OrderGoodsViewSet , OrderInfoViewSet , AlipayView , WeChatNotifyPayView

router = DefaultRouter()
# 购物车
router.register(r'ShoppingCart', ShoppingCartViewSet, basename="ShoppingCart")

# 购物车货物
router.register(r'OrderGoods', OrderGoodsViewSet, basename="OrderGoods")

# 购物车信息
router.register(r'OrderInfo', OrderInfoViewSet, basename="OrderInfo")

# 微信支付
# router.register(r'weixinpay', WeChatNotifyPayView, basename="weixinpay")

app_name = "trade"

urlpatterns = [
    url(r"^", include(router.urls), name="trade"),
]
