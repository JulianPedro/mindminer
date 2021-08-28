from rest_framework_mongoengine import viewsets

from subject.mongo_models import Tweet
from subject.mongo_serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """ Tweet ViewSet with MongoEngine. """
    lookup_field = 'id'
    serializer_class = TweetSerializer
    http_method_names = ['get']

    def get_queryset(self):
        """ Custom get queryset. """
        search = self.request.GET.get('search', None)
        date_from = self.request.GET.get('from', None)
        date_to = self.request.GET.get('to', None)
        queryset = Tweet.objects.all()
        if search:
            queryset = queryset.filter(hashtag__icontains=search)
        if date_from:
            queryset = queryset.filter(tweet_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(tweet_date__lte=date_to)
        return queryset
