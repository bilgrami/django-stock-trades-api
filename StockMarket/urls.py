from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView
from rest_framework import routers
from RestAPI import views
from django.contrib import admin

from django.urls import include, path
from rest_framework import routers


trade_router = routers.DefaultRouter()
trade_router.register('', views.TradeViewSet)

user_router = routers.DefaultRouter()
user_router.register('', views.UserViewSet)

urlpatterns = [
    # Dummy route. Can be removed.
    # url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
    # trade_router.register(r'^erase/', None),
    url(r'^trades/users/', include(user_router.urls)),
    url(r'^trades/', include(trade_router.urls)),
    path('admin/', admin.site.urls),

]

# urlpatterns = format_suffix_patterns(urlpatterns)