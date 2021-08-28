# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import pymongo
from pymongo.errors import DuplicateKeyError

from scrapy.utils.project import get_project_settings
from mindminer.text_classification.classify import Classify


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

    def __init__(self):
        self.classify = Classify(model_json='mindminer/text_classification/model/model.json',
                                 model_hdf5='mindminer/text_classification/model/model.h5',
                                 tokenizer_json='mindminer/text_classification/tokenizer/tokenizer.json',
                                 sentiment_file='mindminer/text_classification/labels/label.pkl')

    def process_item(self, item, spider):
        item['discover_date'] = datetime.datetime.now()
        if item.get('create_at', None):
            item['create_at'] = datetime.datetime.strptime(item.get('create_at'), '%a %b %d %H:%M:%S %z %Y')
        if not item.get('tweet_url') and item.get('user_name') and item.get('tweet_id'):
            user_name = item.get('user_name')
            tweet_id = item.get('tweet_id')
            item['tweet_url'] = f'https://twitter.com/{user_name}/status/{tweet_id}'
        analysis, score = self.classify.classify(item.get('tweet_text'))
        item['captured_by'] = spider.name
        item['analysis_date'] = datetime.datetime.now()
        item['analysis_result'] = analysis
        item['score_result'] = score
        return item
