from django.conf.urls import url
from django.views.decorators.cache import cache_page
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  url(r'anime$', cache_page(60 * 60 * 24)(views.AnimeList.as_view())),
  url(r'genres$', cache_page(60 * 60 * 24)(views.GenresList.as_view())),
  url(r'anime/(?P<pk>[0-9]+)/$', cache_page(60 * 60 * 24)(views.AnimeEntity.as_view())),
  url(r'genres/(?P<pk>[0-9]+)/$', cache_page(60 * 60 * 24)(views.GenresEntity.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)
