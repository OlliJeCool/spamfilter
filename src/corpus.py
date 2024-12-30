import os
from src.exceptions.FolderNotFoundException import FolderNotFoundException
from src.utils import path_exists

class Corpus:
    '''Wrapper of fold of emails for evaluation.'''
    def __init__(self, filepath: str):
        self.filepath = filepath if path_exists(filepath) else None


    def emails(self):
        '''Generator function for getting emails from the corpus.'''
        if not self.filepath:
            raise FolderNotFoundException("Provided directory not found!")
        for file in list(filter(lambda x: not x.startswith("!") ,os.listdir(self.filepath))):
            with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                text = f.read()
                yield file,text