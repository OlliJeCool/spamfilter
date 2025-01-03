from src.tokenizer import MyTokenizer
import math

class NaiveBayes:
    def __init__(self):
        self.word_counts = {"SPAM": {}, "OK": {}}
        self.total_words = {"SPAM": 0, "OK": 0}
        self.doc_counts = {"SPAM": 0, "OK": 0}
        self.total_docs = 0
        self.vocab_size = 0

    def fit(self, label, text):
        self.doc_counts[label] += 1
        self.total_docs += 1
        tokenizer = MyTokenizer()
        words = tokenizer.tokenize(text)
        for word in words:
            if word not in self.word_counts[label]:
                self.word_counts[label][word] = 0
                self.vocab_size += 1
            self.word_counts[label][word] += 1
            self.total_words[label] += 1

    def calculate_probability(self, word, label):
        word_count = self.word_counts[label].get(word, 0)
        total_words = self.total_words[label]
        return (word_count + 1) / (total_words + self.vocab_size)
    
    def predict(self, input):
        tokenizer = MyTokenizer()
        words = tokenizer.tokenize(input)
        spam_prob = math.log(self.doc_counts["SPAM"] / self.total_docs)
        ham_prob = math.log(self.doc_counts["OK"] / self.total_docs)
        for word in words:
            spam_prob += math.log(self.calculate_probability(word, "SPAM"))
            ham_prob += math.log(self.calculate_probability(word, "OK"))

        return "SPAM" if spam_prob > ham_prob else "OK"