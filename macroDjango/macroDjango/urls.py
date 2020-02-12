
from django.conf.urls import url,include
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from macroDjango.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
import xadmin
from trade.views import AlipayView

router = DefaultRouter()
router.get_api_root_view()
urlpatterns = [
    # 主入口
    # url(r'^', include(router)),
    #  后台管理系统
    path('xadmin/' , xadmin.site.urls),

    # 业务api
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^trade/', include('trade.urls', namespace='trade')),
    url(r'^user_operation/', include('user_operation.urls', namespace='user_operation')),
    url(r'^user/', include('user.urls', namespace='user')),

    # restful API
    url(r'' , include(router.urls)) ,
    url(r'^api-auth/', include('rest_framework.urls'),name="api-auth"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^doc/', include_docs_urls(title="电商API"), name="doc"),
    # url(r'^api-token-auth/', views.obtain_auth_token), # 自带的token固定化
    url(r'^api-jwt-auth/' , obtain_jwt_token) , # jwt 插件安装的token
    url(r'^alipay/return/' , AlipayView, name='alipay'),
    url('', include('social_django.urls' , namespace='social')),
    url(r"^login$",obtain_jwt_token),
]