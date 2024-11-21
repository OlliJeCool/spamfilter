import os
from .exceptions.FolderNotFoundException import FolderNotFoundException
from .utils import read_classification_from_file, path_exists
from .confmat import BinaryConfusionMatrix

def quality_score(tp:int, tn:int, fp:int, fn: int) -> int:
    '''Retuns quality index calculated using provided formula.'''
    true_count = tp+tn
    denom = true_count + (10*fp)+fn
    return true_count/denom


def compute_quality_for_corpus(corpus_dir:str):
    '''Evaluates quality of filter.'''
    if not path_exists(corpus_dir):
        raise FolderNotFoundException("Invalid corpus directory.")
    
    truth_dict = read_classification_from_file(os.path.join(corpus_dir, "!truth.txt")) #Takes correct evaluations.
    pred_dict = read_classification_from_file(os.path.join(corpus_dir, "!prediction.txt")) #Takes the filter predictions.
    confmat = BinaryConfusionMatrix("SPAM", "OK") 
    confmat.compute_from_dicts(truth_dict, pred_dict) #Fills confusion matrix from correct values and predictions.
    return quality_score(confmat.tp, confmat.tn, confmat.fp, confmat.fn) #Calculates quality index of predictions.
