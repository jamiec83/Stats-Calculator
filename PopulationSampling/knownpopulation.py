from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Std_Deviation import sd
from marginoferror import marginerror


def ssk(set):
    set = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    s_dev = sd(set)
    width = 0.6
    me = width / 2
    samplesize = square((1.96 * s_dev) / me)
    return samplesize
