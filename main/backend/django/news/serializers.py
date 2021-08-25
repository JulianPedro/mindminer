from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """ News Serializer. """
    class Meta:
        """ Meta class. """
        model = News
        fields = '__all__'
