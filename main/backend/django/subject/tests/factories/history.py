import factory

from django.utils import timezone
from subject.tests.factories.subject import SubjectFactory


class HistoryFactory(factory.django.DjangoModelFactory):
    """ History Factory """
    subject = factory.SubFactory(SubjectFactory)
    date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    approval_percentage = factory.Faker('random_number')
    disapproval_percentage = factory.Faker('random_number')

    class Meta:
        """ History Meta Factory """
        model = 'subject.History'
        django_get_or_create = ('subject',)
