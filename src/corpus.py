import os
from src.exceptions.FolderNotFoundException import FolderNotFoundException


class Corpus:
    def __init__(self, filepath: str):
        self.filepath = filepath if Corpus.path_exists(filepath) else None

    def emails(self):
        if not self.filepath:
            raise FolderNotFoundException("Provided directory not found!")
        for file in list(filter(lambda x: not x.startswith("!") ,os.listdir(self.filepath))):
            with open(os.path.join(self.filepath, file), "rt", encoding="utf-8") as f:
                yield file,f.read()

    @staticmethod
    def path_exists(filepath: str):
        return os.path.isdir(filepath)