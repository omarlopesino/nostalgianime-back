from django.conf.urls import include, url

from . import routers

urlpatterns = [
  url(r'^', include(routers.router.urls)),
]
