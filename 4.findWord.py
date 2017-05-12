#coding=utf-8

import word2vec

word = sys.argv[0]
model = word2vec.load('corpusWord2Vec.bin')
indexes = model.cosine(word.decode)
for index in indexes[0]:
    print (model.vocab[index])
