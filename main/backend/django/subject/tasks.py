import logging
from datetime import datetime

from mindminer.celery import APP
from subject.models import Subject, Timeline

LOGGER = logging.getLogger('subject.tasks')


@APP.task
def register_popular_subject(subject):
    """ Register interest subject to populate crawler database. """
    try:
        db_subject, created = Subject.objects.get_or_create(hashtag=subject,
                                                            defaults={'popularity': 1,
                                                                      'publication_date': datetime.now()})
        if not created:
            db_subject.popularity += 1
            db_subject.save()
    except Exception:
        LOGGER.exception('Error registering a popular subject')


@APP.task
def update_timeline():
    """ Create timeline with crawler informations about Subject. """
    subjects = Subject.objects.filter(no_data=False)
    if subjects.exists():
        for subject in subjects:
            data = {'interaction': 0, 'approval_percentage': 1, 'disapproval_percentage': 1}  # TODO: Crawler Data
            try:
                _ = Timeline.objects.create(subject=subject, **data)
            except Exception:
                LOGGER.exception(f'Error creating timeline for subject {subject}')
