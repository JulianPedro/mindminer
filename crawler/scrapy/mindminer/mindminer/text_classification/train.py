import json
import io
import sys
import logging
import pickle
import argparse
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model, model_from_json
from tensorflow.keras.layers import LSTM, Dense, Dropout, SpatialDropout1D, Embedding


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='MindMiner Training Model')
parser.add_argument('--text-row', dest='text_row_name', required=True, help='Text row name')
parser.add_argument('--sentiment-row', dest='sentiment_row_name', required=True, help='Sentiment row name')
parser.add_argument('--dataset', dest='dataset_path', required=True, help='Dataset path')
parser.add_argument('--epochs', dest='epochs_amount', required=True, help='Epochs')
parser.add_argument('--model-hdf5', dest='model_hdf5', required=False, help='Continue training with model')
parser.add_argument('--model-json', dest='model_json', required=False, help='Continue training with model')

args = parser.parse_args()

text_row_name = args.text_row_name
sentiment_row_name = args.sentiment_row_name
dataset_path = args.dataset_path
epochs_amount = args.epochs_amount
model_hdf5 = args.model_hdf5
model_json = args.model_json

dataset = pd.read_csv(dataset_path, sep=',')
tweets_data = dataset[[text_row_name, sentiment_row_name]]

# Clean neutral values
tweets_data = tweets_data[tweets_data[sentiment_row_name] != 'Neutro']

# Convert sentiment to numeric
sentiment_label = getattr(tweets_data, sentiment_row_name).factorize()
logger.info(f'Sentiment label to numbers: {sentiment_label}')

tweets = getattr(tweets_data, text_row_name).values
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(tweets)

vocab_size = len(tokenizer.word_index) + 1
encoded_docs = tokenizer.texts_to_sequences(tweets)
padded_sequence = pad_sequences(encoded_docs, maxlen=200)

if model_hdf5 and model_json:
    logger.info(f'Init load model!')
    json_file = open(model_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(model_hdf5)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    logger.info(f'Model Sumary: {model.summary()}')
else:
    logger.info(f'Init create model!')
    # Build model
    embedding_vector_length = 32
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_vector_length, input_length=200))
    model.add(SpatialDropout1D(0.25))
    model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    logger.info(f'Model Sumary: {model.summary()}')

# Training
logger.info('Starting training!')
history = model.fit(padded_sequence, sentiment_label[0], validation_split=0.2, epochs=int(epochs_amount), batch_size=32)
logger.info('Finish training!')

# Save model
model_json = model.to_json()
with open('model/model.json', 'w') as json_file:
    json_file.write(model_json)
# Serialize weights to HDF5
model.save_weights('model/model.h5')
logger.info(f'Model saved in the model folder!')

if not model_hdf5 and not model_json:
    # Save tokenizer
    tokenizer_json = tokenizer.to_json()
    with io.open('tokenizer/tokenizer.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(tokenizer_json, ensure_ascii=False))
    logger.info(f'Tokenizer saved in the tokenizer folder!')

    # Save sentiment labels
    with open('labels/label.pkl', 'wb') as pkl_file:
        pickle.dump(sentiment_label, pkl_file)
    logger.info(f'Sentiment label saved in the labels folder!')
