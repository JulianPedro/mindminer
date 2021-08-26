from rest_framework import serializers
from subject.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """ Subject Serializer. """
    class Meta:
        """ Meta class. """
        model = Subject
        fields = '__all__'
