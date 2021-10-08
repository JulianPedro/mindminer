from datetime import datetime

from django.test import TestCase

from news.tests.factories.news import NewsFactory


class NewsTest(TestCase):
    """ News Test """

    @classmethod
    def setUpTestData(cls):
        """ Setup Test Data """
        cls.news = NewsFactory()

    def test_create_news(self):
        self.assertEquals(str(self.news), str(self.news.title))
