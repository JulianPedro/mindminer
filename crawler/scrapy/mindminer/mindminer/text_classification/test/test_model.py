import csv
import argparse
import sys
import os
sys.path.append('../text_classification')
from classify import Classify


parser = argparse.ArgumentParser(description='MindMiner test and validation train')
parser.add_argument('--model-json', dest='model_json', required=True, help='Model json')
parser.add_argument('--model-hdf5', dest='model_hdf5', required=True, help='Model hdf5')
parser.add_argument('--tokenizer-json', dest='tokenizer_json', required=True, help='Tokenizer json')
parser.add_argument('--sentiment-file', dest='sentiment_file', required=True, help='Sentiment file')
parser.add_argument('--epoch', dest='epoch', required=True, help='Epoch')

args = parser.parse_args()

model_json = args.model_json
model_hdf5 = args.model_hdf5
tokenizer_json = args.tokenizer_json
sentiment_file = args.sentiment_file
epoch = args.epoch

total = 0
correct = 0
incorrect = 0

classify = Classify(model_json=model_json,
                    model_hdf5=model_hdf5,
                    tokenizer_json=tokenizer_json,
                    sentiment_file=sentiment_file)

with open('test/test_data.csv', 'r') as file:
    reader = csv.reader(file)
    _ = next(reader)
    for row in reader:
        total += 1
        result, _ = classify.classify(row[0])
        if (result == 'Negativo' and row[1] == '0') or (result == 'Positivo' and row[1] == '1'):
            correct += 1
        else:
            incorrect += 1

with open('test/result.txt', "a") as file:
    file.write('\n')
    file.write('-----------------------\n')
    file.write(f'Epoch: {epoch}\n')
    file.write(f'Total data: {total}\n')
    file.write(f'Correct: {correct}\n')
    file.write(f'Incorrect: {incorrect}\n')

print('--------------------')
print(f'Epoch: {epoch}')
print(f'Total data: {total}')
print(f'Correct: {correct}')
print(f'Incorrect: {incorrect}')
