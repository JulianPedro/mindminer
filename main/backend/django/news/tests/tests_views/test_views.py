from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from news.tests.factories.news import NewsFactory
from news.models import News
from faker import Faker


class NewsTestCase(APITestCase):
    """ News Test Case. """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Data """
        super().setUpClass()
        cls.news_object = NewsFactory.build()
        cls.news_saved = NewsFactory.create()
        cls.client = APIClient()
        cls.news_url = reverse('news')
        cls.faker_obj = Faker()

    def test_if_get_news(self):
        """ Try get news in request API. """
        response = self.client.get(self.news_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(News.objects.count(), 1)
        news = News.objects.get(title=self.news_object.title)
        self.assertEqual(
            news.description,
            self.news_object.description,
        )
        self.assertEqual(
            news.newspaper,
            self.news_object.newspaper,
        )
