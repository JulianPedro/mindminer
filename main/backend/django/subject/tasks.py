import time
import logging
from datetime import datetime

from django.conf import settings

from mindminer.celery import APP
from subject.models import Subject, Timeline
from subject.mongo_models import Tweet
from subject.crawler_client import ScrapyD

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
            subject_tweets = Tweet.objects.filter(hashtag=subject.hashtag)
            interaction = subject_tweets.count()
            approval_percentage = subject_tweets.filter(analysis_result='Positivo').count()
            if approval_percentage:
                approval_percentage = approval_percentage / interaction * 100
            disapproval_percentage = subject_tweets.filter(analysis_result='Negativo').count()
            if disapproval_percentage:
                disapproval_percentage = disapproval_percentage / interaction * 100
            data = {'interaction': interaction, 'approval_percentage': round(approval_percentage, 2),
                    'disapproval_percentage': round(disapproval_percentage, 2)}
            try:
                _ = Timeline.objects.create(subject=subject, **data)
            except Exception:
                LOGGER.exception(f'Error creating timeline for subject {subject}')


@APP.task
def crawling():
    """ This task manage crawling operations. """
    subjects = Subject.objects.all()
    amount_subjects = subjects.count()
    timeslot_per_subject = 3600 / amount_subjects  # One Hour
    scrapyd = ScrapyD(settings.SCRAPYD_HOST, settings.SCRAPYD_PORT)
    for subject in subjects:
        job_id = scrapyd.start(subject.hashtag)
        time.sleep(timeslot_per_subject)
        scrapyd.stop(job_id)
    LOGGER.info('Executed all crawling jobs to all subjects!')