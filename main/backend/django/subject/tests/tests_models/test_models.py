from datetime import datetime

from django.test import TestCase

from subject.tests.factories.subject import SubjectFactory
from subject.tests.factories.timeline import TimelineFactory


class SubjectTest(TestCase):
    """ Subject Test """

    def setUp(self):
        """ Setup Test Data """
        self.subject = SubjectFactory()

    def test_create_subject(self):
        self.assertEquals(str(self.subject), str(self.subject.hashtag))


class TimelineTest(TestCase):
    """ Timeline Test """

    def setUp(self):
        """ Setup Test Data """
        self.timeline = TimelineFactory()

    def test_create_subject(self):
        self.assertEquals(str(self.timeline),
                          f'{self.timeline.subject} - {datetime.strftime(self.timeline.date, "%d/%m/%Y %H:%M:%S")}')
