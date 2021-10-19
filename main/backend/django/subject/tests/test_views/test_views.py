from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from subject.tests.factories.subject import SubjectFactory
from subject.models import Subject
from faker import Faker


class SubjectTestCase(APITestCase):
    """ Subject Test Case. """

    def setUp(self):
        """ Setup Test Data """
        self.subject_saved = SubjectFactory()
        self.client = APIClient()
        self.subject_url = reverse('subject-list')
        self.faker_obj = Faker()

    def test_if_get_subject(self):
        """ Try get subject in request API. """
        response = self.client.get(self.subject_url)
        response_object = response.json()
        response_subjects_count = response_object.get('count')
        response_subject_object = response_object.get('results')[0]
        self.assertEqual(Subject.objects.count(), response_subjects_count)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_subject_object.get('id'), str(self.subject_saved.id))
        self.assertEqual(response_subject_object.get('registration_date'),
                         self.subject_saved.registration_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        self.assertEqual(response_subject_object.get('timeline_set', {}).get('id'),
                         str(self.subject_saved.timeline_set.first().id))

    # TODO: Get subject with search and check if create new subject when not found