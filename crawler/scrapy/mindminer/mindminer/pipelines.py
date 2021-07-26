# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


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
        for data in item:
            if not data:
                raise DropItem('Missing {0}!'.format(data))
        self.collection.insert(dict(item))
        spider.log('Question added to MongoDB database!')
        return item
