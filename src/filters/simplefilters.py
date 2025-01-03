import os
import random
from src.corpus import Corpus
from src.utils import write_classification_to_file, path_exists
from src.exceptions.FolderNotFoundException import FolderNotFoundException
from .basefilter import BaseFilter

class NaiveFilter(BaseFilter):
    '''Filter always classifies as OK, inherits BaseFilter.'''
    def __init__(self):
        super().__init__()
        self.return_value = "OK" #overrides BaseFilter return value
    
class ParanoidFilter(BaseFilter):
    '''Filter always classifies as SPAM, inherits BaseFilter.'''
    def __init__(self):
        super().__init__()
        self.return_value = "SPAM" #overrides BaseFilter return value

class RandomFilter(BaseFilter):
    '''Filter classifies randomly, inherits BaseFilter.'''
    def __init__(self):
        super().__init__()
        self.return_value = ["SPAM", "OK"] #overrides BaseFilter return value
    
    
    def test(self, corpus_path):
        '''Override of BaseFilter Function'''
        if not path_exists(corpus_path):
            raise FolderNotFoundException("Corpus directory does not exist!")
        corpus = Corpus(corpus_path)
        output = {}
        for name, _ in corpus.emails():
            output[name] = random.choice(self.return_value) #random selection instead of a constant one
        write_classification_to_file(os.path.join(corpus_path, "!prediction.txt"), output)       

