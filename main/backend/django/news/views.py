from django.db.models import Q
from rest_framework import viewsets

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """ News Model View Set. """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']
    paginate_by = 10
