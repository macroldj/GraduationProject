
from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .views import BookPostViewSet, BookGetViewSet

router = DefaultRouter()

# 图书信息
router.register(r'getBook', BookGetViewSet, basename="bookInfo")
router.register(r'postBook', BookPostViewSet, basename="bookInfo")

app_name = "user"
urlpatterns = [
    url(r"^", include(router.urls), name="city"),
]
