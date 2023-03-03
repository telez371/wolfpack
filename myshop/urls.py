from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myshop import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    #drf
    # path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('api/v1/', include('routers')),
    path('api/', include('api.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('users/', include('users.urls', namespace='users')),
    path('', include('shop.urls', namespace='shop')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



