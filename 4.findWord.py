#coding=utf-8

import word2vec
import sys

word = sys.argv[1]
model = word2vec.load('corpusWord2Vec.bin')
indexes = model.cosine(word.decode('utf-8'))
for index in indexes[0]:
    print (model.vocab[index])
