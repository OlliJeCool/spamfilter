from simplefilters import BaseFilter
from naive_bayes import NaiveBayes
from trainingcorpus import TrainingCorpus

class MyFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.naivebayes = NaiveBayes()
    
    def train(self, training_corpus_path = ""):
        corpus = TrainingCorpus(training_corpus_path)
        for filename,email in next(corpus.emails()):
            label = corpus.get_class(filename)
            


    def test(self, corpus_path):
        return super().test(corpus_path)