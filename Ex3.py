from collections import Counter
import nltk
from nltk.corpus import PlaintextCorpusReader
from Ex2 import preprocess, stem


corpusdir = 'corpus/'


class TextVector:
    def __init__(self, file_id):
        self.file_id = file_id
        self.words = build_vectors(corpusdir + file_id)


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
        # Create a Corpus with all the data preprocessed with exercise 2 tokenizer
        self.corpus = PlaintextCorpusReader(corpusdir, '.*/*', word_tokenizer=preprocess)
        # Create the vectorial Space, creating each Vector
        self.Text_vectors = []
        for document in self.corpus.fileids():
            self.Text_vectors.append(TextVector(document))


def search_word_in_vector(text_collection, word):
    document_match = []
    stemmed_word = stem([word])[0]
    for Text_vector in text_collection.Text_vectors:
        if stemmed_word in Text_vector.words:
            document_match.append(Text_vector)
    return sorted(document_match, key=lambda document: document.words.get(stemmed_word))


def main():
    text_collection = TextCollection()
    while True:
        query = input("Insert a word: \n")
        print("The recommended documents are (sorted by relevance): \n")
        for document in search_word_in_vector(text_collection, query):
            print(document.file_id)
        print('\n')


main()
