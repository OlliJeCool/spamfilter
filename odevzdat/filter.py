from basefilter import BaseFilter
from naive_bayes import NaiveBayes
from trainingcorpus import TrainingCorpus, Corpus
from handlehtml import gettxt
from utils import write_classification_to_file
import os

class MyFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.naivebayes = NaiveBayes()
    
    def train(self, training_corpus_path=""):
        corpus = TrainingCorpus(training_corpus_path)
        emails = list(corpus.emails())
        
        for name, email in emails:
            label = corpus.get_class(name)
            text = gettxt(email)
            self.naivebayes.fit(label, text)


    def test(self, corpus_path: str):
        corpus = Corpus(corpus_path)
        emails = list(corpus.emails())
        output = {}
        for name, email in emails:
            output[name] = self.naivebayes.predict(email)
            write_classification_to_file(os.path.join(corpus_path, "!prediction.txt"), output)