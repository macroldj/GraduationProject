
from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .views import AttractionsPostViewSet, AttractionsGetViewSet

router = DefaultRouter()

# 图书信息
router.register(r'getAttractions', AttractionsPostViewSet, basename="AttractionsInfo")
router.register(r'postAttractions', AttractionsGetViewSet, basename="AttractionsInfo")

app_name = "Attractions"
urlpatterns = [
    url(r"^", include(router.urls), name="Attractions"),
]
