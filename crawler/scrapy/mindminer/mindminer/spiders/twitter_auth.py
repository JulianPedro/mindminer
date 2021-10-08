import os

import tweepy
from scrapy.spiders import Spider
from scrapy.http import Request

from mindminer.items import Tweet


class TwitterAuth(Spider):
    """ Twitter spider to get Tweets with API authentication. """
    name = 'TwitterAuth'
    allowed_domains = ['twitter.com']
    url = 'https://twitter.com/explore'
    twitter_keys = {
        'consumer_key': os.environ.get('consumer_key'),
        'consumer_secret': os.environ.get('consumer_secret'),
        'access_token_key': os.environ.get('access_token_key'),
        'access_token_secret': os.environ.get('access_token_secret')
    }
    max_tweets = 100

    def __init__(self, query='', *args, **kwargs):
        super().__init__(*args, **kwargs)

        auth = tweepy.OAuthHandler(self.twitter_keys.get('consumer_key'), self.twitter_keys.get('consumer_secret'))
        auth.set_access_token(self.twitter_keys.get('access_token_key'), self.twitter_keys.get('access_token_secret'))

        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.query = query

    def start_requests(self):
        """ Start requests to initial page. """
        yield Request(url=self.url, meta={'handle_httpstatus_all': True}, callback=self.parse_tweets)

    def parse_tweets(self, response):
        """ Get tweets with TweePy. """
        since_id = None
        max_id = -1
        rescue_tweets = 0
        tweets_by_query = self.max_tweets / 2

        while rescue_tweets < self.max_tweets:
            try:
                if max_id <= 0:
                    new_tweets = self.api.search(q=self.query, count=tweets_by_query, tweet_mode='extended',
                                                 since_id=since_id)
                else:
                    new_tweets = self.api.search(q=self.query, count=tweets_by_query, max_id=str(max_id - 1),
                                                 tweet_mode='extended', since_id=since_id)
                if not new_tweets:
                    self.log('No more tweets to rescue!')
                    break

                for new_tweet in new_tweets:
                    value = new_tweet._json
                    tweet = Tweet()
                    tweet['tweet_id'] = value['id']
                    if 'retweeted_status' in value:
                        tweet['tweet_text'] = value['retweeted_status']['full_text']
                    else:
                        tweet['tweet_text'] = value['full_text']
                    tweet['tweet_date'] = value['created_at']
                    tweet['tweet_source'] = value['source']
                    tweet['user_id'] = value['user']['id']
                    tweet['user_name'] = value['user']['screen_name']
                    tweet['user_photo'] = value['user']['profile_image_url']
                    tweet['hashtag'] = self.query
                    yield tweet
                rescue_tweets += len(new_tweets)
                self.log(f'Downloaded {rescue_tweets} tweets!')
                max_id = new_tweets[-1].id
            except tweepy.TweepError as error:
                self.log(f'Tweepy error: {error}')
                break
