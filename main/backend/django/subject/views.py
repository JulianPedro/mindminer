from django.db.models import Q
from rest_framework import viewsets

from subject.models import Subject
from subject.serializers import SubjectSerializer
from subject.tasks import register_popular_subjects


class SubjectViewSet(viewsets.ModelViewSet):
    """ Subject Model View Set. """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']
    paginate_by = 10

    def get_queryset(self):
        """ Custom django get queryset. """
        filter_hashtag = self.request.GET.get('hashtag', '')
        order_by = self.request.GET.getlist('order_by', ['popularity', 'interaction'])
        hashtag_list = filter_hashtag.split(',')
        hashtag_list_q = Q()
        for hashtag in hashtag_list:
            hashtag_list_q.add(Q(hashtag=hashtag), Q.OR)
        new_queryset = Subject.objects.filter(hashtag_list_q, no_data=False).order_by(*order_by)
        if hashtag_list:
            register_popular_subjects.delay(hashtag_list)
        return new_queryset
