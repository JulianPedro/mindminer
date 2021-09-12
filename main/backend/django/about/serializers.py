from rest_framework import serializers
from about.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    """ Training Serializer. """
    class Meta:
        """ Meta class. """
        model = Training
        fields = '__all__'
