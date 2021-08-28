from rest_framework import viewsets
from rest_framework import filters

from subject.models import Subject
from subject.serializers import SubjectSerializer
from subject.tasks import register_popular_subject


class SubjectViewSet(viewsets.ModelViewSet):
    """ Subject Model View Set. """
    queryset = Subject.objects.filter(no_data=False)
    serializer_class = SubjectSerializer
    http_method_names = ['get']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['popularity']
    ordering = ['-popularity']
    paginate_by = 10

    def get_queryset(self):
        """ Custom django get queryset. """
        queryset = super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            queryset = queryset.filter(hashtag__icontains=search)
            register_popular_subject.delay(search)
        return queryset
