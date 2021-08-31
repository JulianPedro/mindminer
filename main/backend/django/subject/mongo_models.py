from mongoengine import Document, EmbeddedDocument, fields


class Tweet(Document):
    """ Tweet Model with MongoEngine. """
    tweet_id = fields.StringField(required=True)
    tweet_text = fields.StringField(required=True)
    tweet_date = fields.DateTimeField(required=True)
    tweet_source = fields.StringField(required=True)
    tweet_url = fields.StringField(required=True)
    user_id = fields.IntField(required=True)
    user_name = fields.StringField(required=True)
    user_photo = fields.StringField(required=True)
    hashtag = fields.StringField(required=True)
    discover_date = fields.DateTimeField(required=True)
    analysis_date = fields.DateTimeField(required=False)
    analysis_result = fields.StringField(required=False)
    captured_by = fields.StringField(required=True)
    score_result = fields.FloatField(required=False)
