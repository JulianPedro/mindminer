import uuid

from django.db import models


class News(models.Model):
    """ Subject Model. """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    newspaper = models.CharField(verbose_name='Newspaper', max_length=200)  # Source
    title = models.CharField(verbose_name='Title', max_length=1000)
    description = models.CharField(verbose_name='Description', max_length=1000)
    source_url = models.URLField(verbose_name='Source URL')
    image_url = models.URLField(verbose_name='Image URL')
    published_at = models.DateTimeField(verbose_name='Published Date')

    class Meta:
        """ Meta Model Subject. """
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['published_at']

    def __str__(self):
        return self.title
