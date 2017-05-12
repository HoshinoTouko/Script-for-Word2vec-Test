#coding=utf-8

import word2vec
import sys


def delRepeat(li):
    result = []
    for item in li:
        if item not in result:
            result.append(item)
    return result


def statWords(li):
    result = {}
    has = []
    for item in li:
        if item in has:
            result[item] += 1
        else:
            has.append(item)
            result[item] = 1
    has = []
    finalResult = {}
    for key, value in result.items():
        if value not in has:
            finalResult[value] = []
            has.append(value)
        finalResult[value].append(key)
    return finalResult


def get(model, word):
    result = []
    try:
        indexes = model.cosine(word)
    except:
        result = [u"没有这个词"]
    else:
        for index in indexes[0]:
            result.append(model.vocab[index])
    return result


def deepGet(model, word, layer):
    global process
    if layer:
        result = []
        datas = get(model, word)
        for data in datas:
            process += 1
            sys.stdout.write("\r")
            print "Process: ", process
            result += deepGet(model, data, layer-1)
        return result
    else:
        return get(model, word)


# word = sys.argv[1]
words = [
    u"心醉神迷",
    u"可口",
    u"全神贯注",
    u"由衷",
    u"好笑",
    u"反复无常",
    u"心眼坏",
    u"失望",
    u"可疑",
    u"妄求",
    u"老处女",
]
model = word2vec.load('data.bin')



deepWord = u"牛排"
# datas = get(model, deepWord)
process = 0
datas = deepGet(model, deepWord, 2)
print u"[查询]: [", deepWord, u"]"
result = statWords(datas)
for key, value in result.items():
    print key, ":"
    for item in value:
        print item,
    print ""


exit()


word = u"高兴"
datas = get(model, word)
for data in datas:
    print data


exit()
for word in words:
    print u"[查询]: [", word, u"]"
    print get(model, word)

exit()
while 1:
    oneWord = u"雷伯涵"
    # oneWord = str(input(u"词语：")).encode("utf-8")
    get(model, oneWord)
    break





