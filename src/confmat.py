class BinaryConfusionMatrix:
    def __init__(self, pos_tag, neg_tag) -> None:
        self.tp, self.tn, self.fp, self.fn = 0, 0, 0, 0
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
    
    def as_dict(self):
        output = {}
        for short in list(filter(lambda x: len(x) == 2, vars(self).keys())):
            output[short] = getattr(self, short)
        return output

    def update(self, truth, prediction):
        tags = (self.pos_tag, self.neg_tag)
        if truth not in tags or prediction not in tags:
            raise ValueError("Value does not match tags.")
        target_attr = ""
        if truth == prediction:
            target_attr = "tp" if truth == self.pos_tag else "tn"
        else:
            target_attr = "fp" if prediction == self.pos_tag and truth == self.neg_tag else "fn"
        
        current_value = getattr(self, target_attr)
        setattr(self, target_attr, current_value + 1)

    def compute_from_dicts(self, truth_dict: dict, pred_dict: dict):
        for k in truth_dict.keys():
            self.update(truth_dict[k], pred_dict[k])

temp = BinaryConfusionMatrix("a", "b")
print(temp.as_dict())