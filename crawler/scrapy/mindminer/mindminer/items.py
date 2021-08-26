# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Tweet(Item):
    tweet_id = Field()
    tweet_text = Field()
    tweet_date = Field()
    tweet_source = Field()
    tweet_url = Field()
    user_id = Field()
    user_name = Field()
    user_photo = Field()
    hashtag = Field()
    discover_date = Field()
    analysis_date = Field()
    score_result = Field()
    captured_by = Field()
