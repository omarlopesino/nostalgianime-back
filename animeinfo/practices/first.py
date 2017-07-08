# Import django in shell.
import django
django.setup()

# Load AnimeInfo model.
from animeinfo.models import AnimeInfo

# Create AnimeInfo entity and save.
info = AnimeInfo(title= "80's", description = "80's are awesome", year = 1980, period_type="decade", genre="all")
info.save()

# Load anime info.
info_loaded = AnimeInfo.objects.get(id = 1)


