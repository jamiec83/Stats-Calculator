from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Std_Deviation import sd
from PopulationSampling.marginoferror import marginerror


def Cochrans(set):
    set = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    p = 0.5
    q = 1 - p
    me = marginerror(set)
    samplesize = (square(1.96) * p * q) / (square(me))
    return samplesize
