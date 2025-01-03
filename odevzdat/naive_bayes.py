from tokenizer import MyTokenizer
import math

swear_words = [
    "anal", "anus", "arse", "ass", "ballsack", "balls", "bastard", "bitch", "biatch", 
    "bloody", "blowjob", "blow job", "bollock", "bollok", "boner", "boob", "bugger", 
    "bum", "butt", "buttplug", "clitoris", "cock", "coon", "crap", "cunt", "damn", 
    "dick", "dildo", "dyke", "fag", "feck", "fellate", "fellatio", "felching", "fuck", 
    "f u c k", "fudgepacker", "fudge packer", "flange", "Goddamn", "God damn", "hell", 
    "homo", "jerk", "jizz", "knobend", "knob end", "labia", "lmao", "lmfao", "muff", 
    "nigger", "nigga", "omg", "penis", "piss", "poop", "prick", "pube", "pussy", "queer", 
    "scrotum", "sex", "shit", "s hit", "sh1t", "slut", "smegma", "spunk", "tit", "tosser", 
    "turd", "twat", "vagina", "wank", "whore", "wtf", "drug"
]

class NaiveBayes:
    def __init__(self):
        self.word_counts = {"SPAM": {}, "OK": {}}
        self.total_words = {"SPAM": 1, "OK": 1}
        self.doc_counts = {"SPAM": 1, "OK": 1}
        self.total_docs = 1
        self.vocab_size = 1

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
            if word.lower() in swear_words:
                spam_prob += 5

            spam_prob += math.log(self.calculate_probability(word, "SPAM"))
            ham_prob += math.log(self.calculate_probability(word, "OK"))

        return "SPAM" if spam_prob > ham_prob else "OK"
