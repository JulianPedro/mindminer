import uuid

from django.db import models


class Training(models.Model):
    """ Training Model. """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    amount_data = models.IntegerField(verbose_name='Amount Data')
    amount_positive = models.IntegerField(verbose_name='Positive Data')
    amount_negative = models.IntegerField(verbose_name='Negative Data')
    epochs = models.IntegerField(verbose_name='Epochs')
    accuracy = models.FloatField(verbose_name='Accuracy')
    correct_classify_percentage = models.FloatField(verbose_name='Correct classify percentage')
    training_date = models.DateTimeField(verbose_name='Training Date')
    training_version = models.CharField(verbose_name='Training version', max_length=80)

    class Meta:
        """ Meta Model Subject. """
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
        ordering = ['-training_date']

    def __str__(self):
        return f'Training - {self.training_version}'
