import requests
from datetime import datetime, timedelta

from django.conf import settings
from django.utils.dateparse import parse_datetime

from mindminer.celery import APP
from subject.models import Subject
from news.models import News


@APP.task
def get_news():
    """ Get news from API. """
    subjects = Subject.objects.filter(no_data=False).order_by('popularity', 'interaction')
    if subjects.exists():
        subjects = subjects[:10]  # Get first 10 objects
        for subject in subjects:
            query = subject.hashtag
            yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

            apikey = settings.NEWS_API_KEY
            try:
                url = f'https://newsapi.org/v2/top-headlines?country=br&q={query}&from={yesterday}&' \
                      f'sortBy=popularity&category=general&apiKey={apikey}'
                request = requests.get(url)
                if request.ok:
                    data = request.json()
                    for article in data.get('articles', []):
                        newspaper = article['source']['name']
                        title = article['title']
                        description = article['description']
                        source_url = article['url']
                        image_url = article['urlToImage']
                        if not image_url:
                            continue
                        published_at = parse_datetime(article['publishedAt'])
                        news, _ = News.objects.get_or_create(source_url=source_url, defaults={
                            'newspaper': newspaper, 'title': title, 'description': description,
                            'image_url': image_url, 'published_at': published_at})
            except requests.exceptions.RequestException:
                continue
