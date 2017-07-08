from . import models
from . import api
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

# ViewSets define the view behavior.
class AnimeInfoViewSet(viewsets.ModelViewSet):
    queryset = models.AnimeInfo.objects.all()
    http_method_names = ['get']
    renderer_classes = (JSONRenderer,)
    serializer_class = api.AnimeInfoSerializer

    def get_queryset(self):
        queryset = models.AnimeInfo.objects.all()
        queryset = self.get_queryset_filter_year(queryset)
        return queryset

    def get_queryset_filter_year(self, queryset):
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(year = year)
        return queryset