import uuid
from datetime import datetime

from django.db import models


class Subject(models.Model):
    """ Subject Model """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    hashtag = models.CharField(verbose_name='Hashtag', max_length=200)
    publication_date = models.DateTimeField(verbose_name='Publication Date')
    registration_date = models.DateTimeField(verbose_name='Registration Date', auto_now_add=True)
    popularity = models.IntegerField(verbose_name='Popularity')
    interaction = models.IntegerField(verbose_name='Interaction')

    class Meta:
        """ Meta Model Subject """
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ['popularity', 'interaction']

    def __str__(self):
        return self.hashtag


class History(models.Model):
    """ History Model """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    subject = models.ForeignKey('subject.Subject', verbose_name='Subject', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Date')
    approval_percentage = models.FloatField(verbose_name='Approval Percentage')
    disapproval_percentage = models.FloatField(verbose_name='Disapproval Percentage')

    class Meta:
        """ Meta Model History """
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
        ordering = ['date']

    def __str__(self):
        return f'{self.subject} - {datetime.strftime(self.date, "%d/%m/%Y %H:%M:%S")}'
