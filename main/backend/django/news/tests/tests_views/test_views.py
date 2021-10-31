from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from news.tests.factories.news import NewsFactory
from news.models import News
from faker import Faker


class NewsTestCase(APITestCase):
    """ News Test Case. """

    def setUp(self):
        """ Setup Test Data """
        self.news_saved = NewsFactory()
        self.client = APIClient()
        self.news_url = reverse('news-list')
        self.faker_obj = Faker()

    def test_if_get_news(self):
        """ Try get news in request API. """
        response = self.client.get(self.news_url)
        response_object = response.json().get('results')[0]
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_object.get('description'), self.news_saved.description)
        self.assertEqual(response_object.get('newspaper'), self.news_saved.newspaper)
