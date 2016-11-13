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

# Tested using preprocess('corpus/corpus-gutenberg/Inferno')