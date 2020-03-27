from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Std_Deviation import sd


def marginerror(set):
    set = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    s_dev = sd(set)
    se = s_dev / (square(len(set)))
    me = round((1.96 * se), 4)
    return me
