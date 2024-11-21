import os
import random
from src.corpus import Corpus
from src.utils import write_classifictaion_to_file
from src.exceptions.FolderNotFoundException import FolderNotFoundException

class BaseFilter:
    def __init__(self):
        self.return_value = ""

    def train(self, training_corpus_path: str = ""):
        pass

    def test(self, corpus_path: str):
        if not Corpus.path_exists(corpus_path):
            raise FolderNotFoundException("Corpus directory does not exist!")
        corpus = Corpus(corpus_path)
        output = {}
        for name in corpus.emails():
            output[name] = self.return_value
        write_classifictaion_to_file(os.path.join(corpus_path, "!prediction.txt"), output)
        



class NaiveFilter(BaseFilter):    
    def __init__(self):
        super().__init__()
        self.return_value = "OK"
    
class ParanoidFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.return_value = "SPAM"

class RandomFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.return_value = ["SPAM", "OK"]
    
    def test(self, corpus_path):
        if not Corpus.path_exists(corpus_path):
            raise FolderNotFoundException("Corpus directory does not exist!")
        corpus = Corpus(corpus_path)
        output = {}
        for name in corpus.emails():
            output[name] = random.choice(self.return_value)
        write_classifictaion_to_file(os.path.join(corpus_path, "!prediction.txt"), output)       

