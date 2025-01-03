from src.filters.myfilter import MyFilter
from src.quality import compute_quality_for_corpus
from src.utils import read_classification_from_file

filter = MyFilter()
filter.train("1")
filter.test("1")
print(compute_quality_for_corpus("1"))
