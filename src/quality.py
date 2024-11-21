def quality_score(tp:int, tn:int, fp:int, fn: int) -> int:
    true_count = tp+tn
    denom = true_count + (10*fp)+fn
    return true_count/denom