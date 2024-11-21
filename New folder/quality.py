import os
from corpus import Corpus
from FolderNotFoundException import FolderNotFoundException
from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix

def quality_score(tp:int, tn:int, fp:int, fn: int) -> int:
    true_count = tp+tn
    denom = true_count + (10*fp)+fn
    return true_count/denom

def compute_quality_for_corpus(corpus_dir:str):
    if not Corpus.path_exists(corpus_dir):
        raise FolderNotFoundException("Invalid corpus directory.")
    
    truth_dict = read_classification_from_file(os.path.join(corpus_dir, "!truth.txt"))
    pred_dict = read_classification_from_file(os.path.join(corpus_dir, "!prediction.txt"))
    confmat = BinaryConfusionMatrix("SPAM", "OK")
    confmat.compute_from_dicts(truth_dict, pred_dict)
    return quality_score(confmat.tp, confmat.tn, confmat.fp, confmat.fn) 
