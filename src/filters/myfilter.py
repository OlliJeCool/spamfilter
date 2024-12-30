from .simplefilters import BaseFilter
from src.naive_bayes import NaiveBayes
from src.trainingcorpus import TrainingCorpus
from src.handlehtml import gettxt

class MyFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.naivebayes = NaiveBayes()
    
    def train(self, training_corpus_path = ""):
        corpus = TrainingCorpus(training_corpus_path)
        for name,text in next(corpus.emails()):
            print(name, text)
            label = corpus.get_class(name)
            text = gettxt(text)
            self.naivebayes.fit((label,text))
        print(self.naivebayes.word_counts)



    def test(self, corpus_path: str):
        return super().test(corpus_path)