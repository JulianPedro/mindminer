import uuid
from datetime import datetime

from django.db import models


class Subject(models.Model):
    """ Subject Model. """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    hashtag = models.CharField(verbose_name='Hashtag', max_length=200)
    publication_date = models.DateTimeField(verbose_name='Publication Date', null=True, blank=True)
    registration_date = models.DateTimeField(verbose_name='Registration Date', auto_now_add=True)
    popularity = models.IntegerField(verbose_name='Popularity', default=0)
    no_data = models.BooleanField(verbose_name='No data found', default=True)

    class Meta:
        """ Meta Model Subject. """
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ['-popularity']

    def __str__(self):
        return self.hashtag


class Timeline(models.Model):
    """ Timeline Model. """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    subject = models.ForeignKey('subject.Subject', verbose_name='Subject', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    interaction = models.IntegerField(verbose_name='Interaction', default=0)
    approval_percentage = models.FloatField(verbose_name='Approval Percentage', default=0)
    disapproval_percentage = models.FloatField(verbose_name='Disapproval Percentage', default=0)

    class Meta:
        """ Meta Model Timeline. """
        verbose_name = 'Timeline'
        verbose_name_plural = 'Timelines'
        ordering = ['-date']

    def __str__(self):
        return f'{self.subject} - {datetime.strftime(self.date, "%d/%m/%Y %H:%M:%S")}'
