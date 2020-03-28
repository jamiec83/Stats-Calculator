from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Std_Deviation import sd

def skew(set):
    set = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    me = mean(set)
    med = median(set)
    std = sd(set)
    sk = (3*(me-med)/std)
    return sk