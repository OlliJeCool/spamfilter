import os
from src.corpus import Corpus
from src.utils import read_classification_from_file

class TrainingCorpus(Corpus):
    '''Corpus for training which wraps emails and their correct evaluation.'''
    def __init__(self, filepath):
        super().__init__(filepath)
        self.classification = read_classification_from_file(os.path.join(filepath, "!truth.txt")) #Stores all correct evaluations in a dictionary.


    def get_class(self, name: str) -> str:
        '''Returns the emails correct evaulation class.'''
        return self.classification[name]

    def is_ham(self, name: str) -> bool:
        '''Determines if the email evaulation is OK.'''
        return self.classification[name] == "OK"
    
    def is_spam(self, name: str) -> bool:
        '''Determines if the email evaulation is SPAM.'''
        return self.classification[name] == "SPAM"
    
    def spams(self):
        '''Genegator function for getting spam emails from the training corpus.'''
        for file in list(filter(lambda x: not x.startswith("!"), os.listdir(self.filepath))):
            if not self.is_ham(file):
                with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                    yield file, f.read()

    def hams(self):
        '''Genegator function for getting ham emails from the training corpus.'''
        for file in list(filter(lambda x: not x.startswith("!"), os.listdir(self.filepath))):
            if not self.is_spam(file):
                with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                    yield file, f.read()