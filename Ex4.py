from nltk.tokenize import word_tokenize
from nltk.corpus import PlaintextCorpusReader
import math


def list_of_lists(corpus):
    list_of_files = corpus.fileids()
    list_of_l = dict()
    for file in list_of_files:
        list_of_l[file] = corpus.words(file)
    return list_of_l


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(tokenized_text):
    vector = dict()
    for token in tokenized_text:
        if token in vector:
            vector[token] += 1
        else:
            vector[token] = 1
    return vector


def calculate_matrix(list_of_list):
    matrix = dict()
    for list_i in list_of_list:
        for list_j in list_of_list:
            matrix[(list_i, list_j)] = get_cosine(text_to_vector(list_i), text_to_vector(list_j))
    return matrix


def most_similar(matrix, lol, document):
    keys = list(lol.keys())
    list_similar = []
    for i in range(5):
        the_most_similar = ''
        similarity_rating = 0
        for key in keys:
            if document != key:
                if matrix[(document, key)] > similarity_rating:
                    similarity_rating = matrix[(document, key)]
                    the_most_similar = key
        list_similar.append(the_most_similar)
        keys.remove(the_most_similar)
    return list_similar


def main():
    corpus = PlaintextCorpusReader('corpus/corpus-gutenberg', '.*/*')
    lol = list_of_lists(corpus)
    matrix = calculate_matrix(lol)
    while True:
        print('Available documents are: \n')
        keys = lol.keys()
        for key in keys:
            print(key)
        query = input("Search for a similar document: \n")
        similars = most_similar(matrix, lol, query)
        print('\n')
        for similar in similars:
            print(similar)
        print('\n')


main()
