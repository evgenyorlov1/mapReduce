import csv
import nltk
import os
import string
import operator

directory = 'chunks'


def mapfunc():
    for filename in os.listdir(directory):
        print filename
        with open(os.path.join(directory, filename)) as file:
            raw = file.read().lower()
            os.remove(os.path.join(directory, filename))
            tokens = nltk.word_tokenize(raw.translate(None, string.punctuation))
            d = {tokens.count(x):x for x in tokens}
            sorted_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
            with open(os.path.join(directory, filename), 'w') as csvfile:
                for tkn in sorted_d:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(tkn)