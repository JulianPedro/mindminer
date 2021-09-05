from django.db.models import OuterRef, Subquery

from rest_framework import viewsets
from rest_framework import filters

from subject.models import Subject, Timeline
from subject.serializers import SubjectSerializer
from subject.tasks import register_popular_subject


class SubjectViewSet(viewsets.ModelViewSet):
    """ Subject Model View Set. """
    latest_timeline = Timeline.objects.filter(subject_id=OuterRef('id')).order_by('-date')
    approval_percentage = latest_timeline.values_list('approval_percentage')[:1]
    disapproval_percentage = latest_timeline.values_list('disapproval_percentage')[:1]
    queryset = Subject.objects.filter(no_data=False).annotate(approval_percentage=Subquery(approval_percentage),
                                                              disapproval_percentage=Subquery(disapproval_percentage))
    serializer_class = SubjectSerializer
    http_method_names = ['get']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['hashtag', 'popularity', 'approval_percentage', 'disapproval_percentage']
    ordering = ['-popularity']
    paginate_by = 10

    def get_queryset(self):
        """ Custom django get queryset. """
        queryset = super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            queryset = queryset.filter(hashtag__icontains=search)
            if len(search) >= 2:  # Skip possible wrong search
                register_popular_subject.delay(search)
        return queryset
