import json
import pickle
import logging
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import model_from_json


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)


class Classify:
    def __init__(self, *args, **kwargs):
        model_json = kwargs.get('model_json')
        model_hdf5 = kwargs.get('model_hdf5')
        tokenizer_json = kwargs.get('tokenizer_json')
        sentiment_file = kwargs.get('sentiment_file')
        self.model = self.load_json_model(model_json, model_hdf5)
        self.tokenizer = self.load_json_tokenizer(tokenizer_json)
        self.sentiments = self.load_sentiment_labels(sentiment_file)

    @staticmethod
    def load_json_model(model_json, model_hdf5):
        json_file = open(model_json, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(model_hdf5)
        logger.info('Model loaded from disk!')
        return loaded_model

    @staticmethod
    def load_json_tokenizer(tokenizer_json):
        json_file = open(tokenizer_json, 'r')
        loaded_tokenizer_json = json_file.read()
        data = json.loads(loaded_tokenizer_json)
        json_file.close()
        tokenizer = tokenizer_from_json(data)
        return tokenizer

    @staticmethod
    def load_sentiment_labels(sentiment_file):
        pkl_file = open(sentiment_file, 'rb')
        return pickle.load(pkl_file)

    def classify(self, text):
        texts = self.tokenizer.texts_to_sequences([text])
        texts = pad_sequences(texts, maxlen=200)
        score = self.model.predict(texts)
        prediction = int(score.round().item())
        return score, self.sentiments[1][prediction]
