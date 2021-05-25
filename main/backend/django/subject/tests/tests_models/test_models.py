from datetime import datetime

from django.test import TestCase

from subject.tests.factories.subject import SubjectFactory
from subject.tests.factories.history import HistoryFactory


class SubjectTest(TestCase):
    """ Subject Test """

    @classmethod
    def setUpTestData(cls):
        """ Setup Test Data """
        cls.subject = SubjectFactory()

    def test_create_subject(self):
        self.assertEquals(str(self.subject), str(self.subject.hashtag))


class HistoryTest(TestCase):
    """ History Test """

    @classmethod
    def setUpTestData(cls):
        """ Setup Test Data """
        cls.history = HistoryFactory()

    def test_create_subject(self):
        self.assertEquals(str(self.history),
                          f'{self.history.subject} - {datetime.strftime(self.history.date, "%d/%m/%Y %H:%M:%S")}')
