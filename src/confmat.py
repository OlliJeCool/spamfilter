class BinaryConfusionMatrix:
    '''Basic confusion matrix implementation.'''
    def __init__(self, pos_tag, neg_tag) -> None:
        self.tp, self.tn, self.fp, self.fn = 0, 0, 0, 0
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
    

    def as_dict(self):
        '''Returns matrix valuse in a dictionary.'''
        output = {}
        for short in list(filter(lambda x: len(x) == 2, vars(self).keys())): #filters out pos and neg tag attributes
            output[short] = getattr(self, short) #gets values of attributes and adds them to dictionary
        return output

    def update(self, truth, prediction):
        '''Evaluates prediction and updates the matrix.'''
        tags = (self.pos_tag, self.neg_tag) 
        if truth not in tags or prediction not in tags: #edge case when some of the inputed values is not a tag
            raise ValueError("Value does not match tags.")
        target_attr = ""
        #attribute selection logic
        if truth == prediction:
            target_attr = "tp" if truth == self.pos_tag else "tn"
        else:
            target_attr = "fp" if prediction == self.pos_tag and truth == self.neg_tag else "fn"
        
        #gets the current value and increases it by 1
        current_value = getattr(self, target_attr)
        setattr(self, target_attr, current_value + 1)


    def compute_from_dicts(self, truth_dict: dict, pred_dict: dict):
        '''Takes two dictionaries and updates the matrix accordingly.'''
        for k in truth_dict.keys():
            self.update(truth_dict[k], pred_dict[k])