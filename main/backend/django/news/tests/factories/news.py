import factory

from django.utils import timezone


class NewsFactory(factory.django.DjangoModelFactory):
    """ News Factory """
    newspaper = factory.Faker('sentence', nb_words=1)
    title = factory.Faker('sentence', nb_words=1)
    description = factory.Faker('sentence', nb_words=1)
    source_url = 'https://testurl.com/'
    image_url = 'https://imageurl.com/'
    published_at = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())

    class Meta:
        """ News Meta Factory """
        model = 'news.News'
        django_get_or_create = ('title',)
