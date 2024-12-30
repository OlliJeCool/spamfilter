import string

class MyTokenizer:
    @staticmethod
    def tokenize(text: str):
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        return words
