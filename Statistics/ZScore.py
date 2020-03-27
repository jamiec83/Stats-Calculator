from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Std_Deviation import sd


def ZScore(num):
    z_mean = mean(num)
    sdev = sd(num)
    z_list = []
    for x in num:
        z = round(((x - z_mean) / sdev), 6)
        z_list.append(z)
    return z_list
