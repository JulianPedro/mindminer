import factory

from django.utils import timezone


class SubjectFactory(factory.django.DjangoModelFactory):
    """ Subject Factory """
    hashtag = factory.Faker('sentence', nb_words=1)
    publication_date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    registration_date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    popularity = factory.Faker('random_number')

    class Meta:
        """ Subject Meta Factory """
        model = 'subject.Subject'
        django_get_or_create = ('hashtag',)
