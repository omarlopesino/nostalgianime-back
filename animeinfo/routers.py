from rest_framework import routers
from . import serializers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'anime', serializers.AnimeInfoViewSet)
