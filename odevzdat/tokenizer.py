import string

class MyTokenizer:
    @staticmethod
    def tokenize(text: str):
        if(type(text) != str):
            return []
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Split text into words
        words = text.split()
        # Remove numbers and apply basic stemming
        words = [MyTokenizer.stem(word) for word in words if not word.isdigit()]
        return words

    @staticmethod
    def stem(word: str):
        # Basic stemming: remove common suffixes
        suffixes = ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']
        for suffix in suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                return word[:-len(suffix)]
        return word