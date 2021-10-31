from django.test import TransactionTestCase
from celery.contrib.testing.worker import start_worker

from mindminer.celery import APP
from news.tasks import get_news


class GetNewsTestCase(TransactionTestCase):
    """ Get News Test Case. """
    @classmethod
    def setUpClass(cls):
        """ SetUp Class. """
        super().setUpClass()
        cls.celery_worker = start_worker(APP, perform_ping_check=False)
        cls.celery_worker.__enter__()

    @classmethod
    def tearDownClass(cls):
        """ Tear Down Class. """
        super().tearDownClass()
        cls.celery_worker.__exit__(None, None, None)

    def setUp(self):
        """ SetUp. """
        super().setUp()
        self.task = get_news.delay()
        self.results = self.task.get()

    def test_success(self):
        """ Test if get news works. """
        self.assertEqual(self.task.state, 'SUCCESS')
