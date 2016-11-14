import os
from collections import Counter
import nltk
from os import walk

from nltk.corpus import PlaintextCorpusReader

from Ex1 import tokenize, count_words

corpusdir = 'corpus/'


class TextVector:
    def __init__(self, file_id):
        self.file_id = file_id
        self.vectors = build_vectors(file_id)


def build_vectors(text):
    """
    Method that receives a text and returns the dict with the words and count of each word.
    :param text: url of the text
    :return: dict with the words and count of each word
    """
    raw = open(text, 'rU').read()
    tokens = nltk.word_tokenize(raw)
    # used later for giving the size of the vector.
    amount_of_words = len(tokens)
    counter = Counter()
    for token in tokens:
        counter[token] += 1

    dictionary = dict(counter)
    # Creates the vector size
    for key, value in dictionary.items():
        dictionary[key] = value / amount_of_words
    return dictionary


class TextCollection:
    def __init__(self):
        # Create a Corpus with all the data
        self.corpus = PlaintextCorpusReader(corpusdir, '.*/*')
        # Create the vectorial Space, creating each Vector
        self.vectors = []
        for document in self.corpus.fileids():
            self.vectors.append(TextVector(document))


def main():
    text_collection = TextCollection()
    while True:
        text_name = input("Insert a Query")


main()
