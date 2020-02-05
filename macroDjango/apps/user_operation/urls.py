from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from user_operation.views import UserAddressViewSets , UserFavViewSets , UserViewSets , UserLeavingMessageViewSets

router = DefaultRouter()
# 用户操作
router.register(r'UserAddress', UserAddressViewSets, basename="UserAddress")
router.register(r'UserFav', UserFavViewSets, basename="UserFav")
router.register(r'User', UserViewSets, basename="User")
router.register(r'UserLeavingMessage', UserLeavingMessageViewSets, basename="UserLeavingMessage")

app_name = 'user_operation'
urlpatterns = [
    url(r"^", include(router.urls), name="user_operation"),
]
