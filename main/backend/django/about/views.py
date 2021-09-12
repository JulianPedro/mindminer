from rest_framework import viewsets

from about.models import Training
from about.serializers import TrainingSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    """ Training Model View Set. """
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    http_method_names = ['get']