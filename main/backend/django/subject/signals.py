from django.dispatch import receiver
from django.db.models.signals import post_save

from subject.models import Subject, Timeline


@receiver(post_save, sender=Subject)
def create_first_timeline(sender, instance, created, **kwargs):  # pylint:disable=unused-argument
    if created:
        Timeline.objects.create(subject=instance)
