""""Anime info model."""
from django.db import models
from django.utils.translation import ugettext as _
from .includes import animeinfo_options
import datetime

class AnimeInfo(models.Model):
    "Show anime info of a period (year, decade, etc)"
    title = models.CharField(max_length = 200)
    period_type = models.CharField(max_length = 50, choices = animeinfo_options.PERIODS, default = 'decade')
    description = models.TextField()
    year = models.IntegerField(_('year'), choices= animeinfo_options.YEAR_CHOICES, default=datetime.datetime.now().year)
    image = models.ImageField(upload_to = 'animeinfo')
    genre = models.CharField(max_length = 50, choices = animeinfo_options.GENRES, default = 'all')

    def __str__(self):
        return self.title
