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
        queryset = Tweet.objects.all()
        if search:
            queryset = queryset.filter(hashtag__icontains=search)
        return queryset
