
from django.conf.urls import url,include
from django.urls import path
from macroDjango.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
import xadmin

urlpatterns = [
    # 主入口
    # url(r'^', include(router)),
    #  后台管理系统
    path('xadmin/' , xadmin.site.urls),

    # 业务api
    url(r'^v1/goods/', include('goods.urls', namespace='goods')),
    url(r'^v1/trade/', include('trade.urls', namespace='trade')),
    url(r'^v1/user_operation/', include('user_operation.urls', namespace='user_operation')),
    url(r'^v1/user/', include('user.urls', namespace='user')),

    # restful API
    url(r'^api-auth/', include('rest_framework.urls'),name="api-auth"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^doc/', include_docs_urls(title="电商API"),name="doc")
]