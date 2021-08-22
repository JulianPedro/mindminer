import json
import io
import sys
import logging
import pickle
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, SpatialDropout1D, Embedding


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

text_row_name = sys.argv[1]
sentiment_row_name = sys.argv[2]
dataset_path = sys.argv[3]
epochs_amount = sys.argv[4]

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

# Save tokenizer
tokenizer_json = tokenizer.to_json()
with io.open('tokenizer/tokenizer.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json.dumps(tokenizer_json, ensure_ascii=False))
logger.info(f'Tokenizer saved in the tokenizer folder!')

# Save sentiment labels
with open('labels/label.pkl', 'wb') as pkl_file:
    pickle.dump(sentiment_label, pkl_file)
logger.info(f'Sentiment label saved in the labels folder!')
