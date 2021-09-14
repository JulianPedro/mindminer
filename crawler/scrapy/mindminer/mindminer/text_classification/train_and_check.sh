#!/usr/bin/bash

runedEpochs=40

while [ $runedEpochs -lt $1 ]
do
    python3 train.py --text-row tweet_text --sentiment-row sentiment --dataset ../../../../../archive/dataset_completed_cleaned.csv --epochs 1 --model-hdf5 model/model.h5 --model-json model/model.json
    runedEpochs=`expr $runedEpochs + 1`
    python3 test/test_model.py --model-json model/model.json --model-hdf5 model/model.h5 --tokenizer-json tokenizer/tokenizer.json --sentiment-file labels/label.pkl --epoch $runedEpochs
done
