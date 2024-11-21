import os

class Corpus:
    def __init__(self, emailpath):
        self.emailpath = emailpath

    def file_exists(self):
        if not os.path.isfile(self.emailpath):
            raise FileNotFoundError

    def emails(self):
        self.file_exists()
        filenames = list(lambda start: start[0] == "!", filter(os.listdir(self.emailpath)))

        for filename in filenames:
            with open(filename, "r", encoding="utf-8") as r:
                text = r.readline()
            yield text.split()[0]
            yield text.split()[1]






