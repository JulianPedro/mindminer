import logging
import requests
import random
import urllib.parse

LOGGER = logging.getLogger('subject.crawler_client')

SPIDERS = ['TwitterAuth', 'TwitterNoAuth']


class ScrapyD:
    """ ScrapyD client. """

    def __init__(self, host, port, spider=None, project='default'):
        self.spider_name = spider
        self.project = project
        self.path_schedule = 'schedule.json'
        self.path_cancel = 'cancel.json'
        self.scrapyd = f'http://{host}:{port}'

    @property
    def spider(self):
        """ Get spider name. """
        if not self.spider_name or self.spider_name not in SPIDERS:
            return SPIDERS[random.randint(0, 1)]
        return self.spider_name

    @staticmethod
    def client(full_url, data):
        """ Client request crawler. """
        result = requests.post(full_url, data=data)
        return result.json()

    def start(self, query):
        """ Start spider. """
        data = {'spider': self.spider, 'project': self.project, 'query': query}
        try:
            result = self.client(urllib.parse.urljoin(self.scrapyd, self.path_schedule), data)
        except Exception as error:
            LOGGER.exception('Schedule request error!')
        else:
            return result.get('jobid')

    def stop(self, job_id):
        """ Stop spider. """
        data = {'project': self.project, 'job': job_id}
        try:
            result = self.client(urllib.parse.urljoin(self.scrapyd, self.path_cancel), data)
        except Exception as error:
            LOGGER.exception('Cancel request error!')
        else:
            return result.get('status')
