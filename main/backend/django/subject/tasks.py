from datetime import datetime

from mindminer.celery import APP
from subject.models import Subject


@APP.task
def register_popular_subjects(subjects):
    """ Register interest subject to populate crawler database. """
    for subject in subjects:
        db_subject, created = Subject.objects.get_or_create(hashtag=subject,
                                                            defaults={'popularity': 1,
                                                                      'publication_date': datetime.now()})
        if not created:
            db_subject.popularity += 1
            db_subject.save()
