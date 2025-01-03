import os
from utils import path_exists

class Corpus:
    '''Wrapper of fold of emails for evaluation.'''
    def __init__(self, filepath: str):
        self.filepath = filepath if path_exists(filepath) else None


    def emails(self):
        '''Generator function for getting emails from the corpus.'''
        for file in list(filter(lambda x: not x.startswith("!") ,os.listdir(self.filepath))):
            with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                text = f.read()
                if not text:
                    text = ""
                yield file,text