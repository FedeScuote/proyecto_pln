import matplotlib.pyplot as plt
import operator
import os
import nltk
from collections import Counter



def tokenize(text_name):
    """
    1)
    :param text_name: receives the name of a text
    :return: returns a list of tokens in that archive
    """
    raw = open(text_name, 'rU').read()
    tokens = nltk.word_tokenize(raw)
    return tokens


def count_words(corpus_root):
    """
    2)
    :param corpus_root: receives the full path of the corpus location
    :return: a dictionary that maps for every word on the corpus, the number of ocurrences
    """
    tokens = []
    for root, dirs, files in os.walk(corpus_root):
        for filename in files:
            tokens.extend(tokenize(os.path.join(root, filename)))
    counter = Counter()
    for token in tokens:
        counter[token] += 1
    return counter


def sort_words(dict):
    """
    3)
    :param dict: Receives a dictionary of words
    :return: returns a sorted list of the words in dict, sorted by amount of occurrences
    """
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)


def zipf_law(sorted_list):
    """
    4)
    :param sorted_list: receives a sorted list of the corpus, sorted by amount of occurrences
    :return: a list of tuples that can be analyzed for zipf_law for the first 100 words
    """
    zipfs_law = []
    ranked_list = enumerate(sorted_list[10:100])
    for rank, (word, count) in ranked_list:
        zipfs_law.append((word, count, rank + 1, count * (rank + 1)))

    counts = [token[1] for token in zipfs_law]
    ranks = [token[2] for token in zipfs_law]
    plt.plot(ranks, counts)
    plt.ylabel('counts')
    plt.xlabel('ranks')
    plt.show()


