from collections import Counter
import nltk
from Ex1 import tokenize, count_words


class textVector():
    def __init__(self, text_name):
        self.text_name = text_name
        self.vectors = build_vectors(text_name)


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
