from rest_framework_mongoengine import serializers

from subject.mongo_models import Tweet


class TweetSerializer(serializers.DocumentSerializer):
    """ Tweet Serializer with MongoEngine. """

    class Meta:
        """ Meta Serializer """
        model = Tweet
        fields = '__all__'
