import os
from collections import Counter

import nltk
import Ex1


def preprocess(file):
    """
    1)
    :param file: receives a filename
    :return: list of tokens, non capital letters, and stemmed
    """
    tokens = Ex1.tokenize(file)
    return stem(tokens)


def stem(tokens):
    """
    grabs tokens, converts them to lower case and stems them
    :param tokens: tokens from text
    :return: stemmed text
    """
    porter = nltk.PorterStemmer()
    lowered_tokens = []
    stemmed = []
    for token in tokens:
        lowered_tokens.append(token.lower())
    for lowered_token in lowered_tokens:
        stemmed.append(porter.stem(lowered_token))
    return stemmed


def count_words(corpus_root):
    """
    2)
    :param corpus_root: receives the full path of the corpus location
    :return: a dictionary that maps for every word on the corpus, the number of ocurrences
    """
    tokens = []
    for root, dirs, files in os.walk(corpus_root):
        for filename in files:
            tokens.extend(preprocess(os.path.join(root, filename)))
    counter = Counter()
    for token in tokens:
        counter[token] += 1
    return counter

# Tested using preprocess('corpus/corpus-gutenberg/Inferno')