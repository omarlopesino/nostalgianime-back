"""Options lists for animeinfo model."""
import datetime
from django.utils.translation import ugettext as _
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# @TODO: add rest of GENRES, or only main!
GENRES = [
    ('all', _('All')),
    ('action', _('Action')),
    ('adventure', _('Adventure')),
    ('comedy', _('Comedy')),
    ('drama', _('Drama')),
    ('sci-fi', _('Sci-fi')),
    ('space', _('Space')),
    ('mistery', _('Mistery')),
    ('supernatural', _('Supernatural')),
    ('police', _('Police'))
]

PERIODS = [
    ('year', _('Year')),
    ('decade', _('Decade')),
]