from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """ News Model View Set. """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    http_method_names = ['get']
    filterset_fields = ['newspaper', 'title', 'published_at']
    ordering_fields = ['published_at']
    ordering = ['-published_at']
    paginate_by = 10
