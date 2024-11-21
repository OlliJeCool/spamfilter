import os
from src.corpus import Corpus
from src.exceptions.FolderNotFoundException import FolderNotFoundException
from src.utils import read_classification_from_file

class TrainingCorpus(Corpus):
    def __init__(self, filepath):
        super().__init__(filepath)
        if not Corpus.path_exists(self.filepath):
            raise FolderNotFoundException("Corpus folder not found.")
        self.classification = read_classification_from_file(os.path.join(filepath, "!truth.txt"))

    def get_class(self, name: str) -> str:
        return self.classification[name]

    def is_ham(self, name: str) -> bool:
        return self.classification[name] == "OK"
    
    def is_spam(self, name: str) -> bool:
        return self.classification[name] == "SPAM"
    
    def spams(self):
        for file in list(filter(lambda x: not x.startswith("!"), os.listdir(self.filepath))):
            if self.is_ham(file):
                continue
            with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                yield file, f.read()

    def hams(self):
        for file in list(filter(lambda x: not x.startswith("!"), os.listdir(self.filepath))):
            if self.is_spam(file):
                continue
            with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                yield file, f.read()