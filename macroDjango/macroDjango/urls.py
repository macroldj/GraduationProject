"""macroDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.urls import path
from macroDjango.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet , CategoryViewset , IndexCategoryViewset , BannerViewset , HotSearchsViewset
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin


router = DefaultRouter()
# 电商的商品列表
router.register(r'goods', GoodsListViewSet)

# Category url
router.register(r'Category', CategoryViewset)

#轮播图url
router.register(r'banners', BannerViewset, basename="banners")

#首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")

# main url
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{"document_root": MEDIA_ROOT}),
    url(r'^api/', include('rest_framework.urls')),
    url(r'doc/', include_docs_urls(title="生鲜电商"))
]

