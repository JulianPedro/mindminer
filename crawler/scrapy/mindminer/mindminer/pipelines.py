# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import pymongo
from pymongo.errors import DuplicateKeyError

from scrapy.utils.project import get_project_settings


class MongoDBPipeline:
    """ Pipeline to save data in MongoDB. """
    settings = get_project_settings()

    def __init__(self):
        connection = pymongo.MongoClient(host=self.settings['MONGODB_SERVER'], port=self.settings['MONGODB_PORT'],
                                         username=self.settings['MONGODB_USERNAME'],
                                         password=self.settings['MONGODB_PASSWORD'])
        db = connection[self.settings['MONGODB_DB']]
        self.collection = db[self.settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        try:
            self.collection.insert(dict(item))
        except DuplicateKeyError:
            spider.log('Item already exists! Pass')
        spider.log('Question added to MongoDB database!')
        return item


class DataPipeline:
    """ Pipeline to add metadata in items. """

    def process_item(self, item, spider):
        item['discover_date'] = datetime.datetime.now()
        if not item.get('tweet_url') and item.get('user_name') and item.get('tweet_id'):
            user_name = item.get('user_name')
            tweet_id = item.get('tweet_id')
            item['tweet_url'] = f'https://twitter.com/{user_name}/status/{tweet_id}'
        item['captured_by'] = spider.name
        item['analysis_date'] = None
        item['analysis_result'] = None
        item['positive_result'] = None
        item['negative_result'] = None
        return item
