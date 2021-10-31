from django.test import TransactionTestCase
from celery.contrib.testing.worker import start_worker

from mindminer.celery import APP
from subject.tasks import register_popular_subject, update_timeline


class RegisterPopularSubjectTestCase(TransactionTestCase):
    """ Register Popular Subject Test Case. """
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
        self.task = register_popular_subject.delay('bar')
        self.results = self.task.get()

    def test_success(self):
        """ Teste if success when execute. """
        self.assertEqual(self.task.state, 'SUCCESS')


class UpdateTimelineTestCase(TransactionTestCase):
    """ Update Timeline Test Case. """
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
        self.task = update_timeline.delay()
        self.results = self.task.get()

    def test_success(self):
        """ Teste if success when execute. """
        self.assertEqual(self.task.state, 'SUCCESS')


