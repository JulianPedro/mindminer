from rest_framework import serializers
from subject.models import Subject, Timeline


class TimelineSerializer(serializers.ModelSerializer):
    """ Subject Serializer. """

    class Meta:
        """ Meta class. """
        model = Timeline
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    """ Subject Serializer. """
    timeline_set = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """ Meta class. """
        model = Subject
        fields = '__all__'
        depth = 3

    def get_timeline_set(self, obj):
        """ Override timeline_set to get first latest timeline. """
        latest_timeline = obj.timeline_set.first()
        if latest_timeline:
            return TimelineSerializer(latest_timeline).data
