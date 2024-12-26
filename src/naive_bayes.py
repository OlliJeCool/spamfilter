class NaiveBayes:
    def __init__(self):
        self.word_counts = {"spam": {}, "ham": {}}
        self.total_words = {"spam": 0, "ham": 0}
        self.doc_counts = {"spam": 0, "ham": 0}
        self.total_docs = 0

    def fit(self, data):
        for text, label in data:
            self.doc_counts[label] += 1
            self.total_docs += 1
            words = text
            for word in words:
                if word not in self.word_counts[label]:
                    self.word_counts[label][word] = 0
                self.word_counts[label][word] += 1
                self.total_words[label] += 1
    
    def calculate_probability(self, word, label):
        word_count = self.word_counts[label].get(word, 0)
        total_words = self.total_words[label]
        vocab_size = len(set(list(self.word_counts["spam"].keys()) + list(self.word_counts["ham"].keys())))
        return (word_count + 1) / (total_words+ vocab_size)
    
    def predict(self, input):
        words = input
        spam_prob = self.doc_counts["spam"] / self.total_docs
        ham_prob = self.doc_counts["ham"] / self.total_docs
        for word in words:
            spam_prob *= self.calculate_probability(word, "spam")
            ham_prob *= self.calculate_probability(word, "ham")

        return "SPAM" if spam_prob > ham_prob else "OK"