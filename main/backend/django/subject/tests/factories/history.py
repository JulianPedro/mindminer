import factory

from django.utils import timezone
from subject.tests.factories.subject import SubjectFactory


class TimelineFactory(factory.django.DjangoModelFactory):
    """ Timeline Factory """
    subject = factory.SubFactory(SubjectFactory)
    date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    interaction = factory.Faker('random_number')
    approval_percentage = factory.Faker('random_number')
    disapproval_percentage = factory.Faker('random_number')

    class Meta:
        """ Timeline Meta Factory """
        model = 'subject.Timeline'
        django_get_or_create = ('subject',)
