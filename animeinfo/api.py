from . import models
from rest_framework import serializers

# Serializers define the API representation.
class AnimeInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AnimeInfo
        #fields = ('title',)
        fields = '__all__'
