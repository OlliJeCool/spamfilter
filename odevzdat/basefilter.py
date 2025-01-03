import os
from corpus import Corpus
from utils import write_classification_to_file

class BaseFilter:
    '''Base class for other filters.'''
    def __init__(self):
        self.return_value = "" #default return value

    def train(self, training_corpus_path: str = ""): 
        pass #not implemented for now

    def test(self, corpus_path: str):
        '''Tests emails from the provided corpus.'''
        corpus = Corpus(corpus_path)
        output = {}
        for name, _ in corpus.emails():
            output[name] = self.return_value
        write_classification_to_file(os.path.join(corpus_path, "!prediction.txt"), output)
        
