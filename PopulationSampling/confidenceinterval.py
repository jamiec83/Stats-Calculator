from Calculator.Square import square
from Statistics.Mean import mean
from Statistics.Std_Deviation import sd


def ConfInt():
    set = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    ci_mean = mean(set)
    s_dev = sd(set)
    ci_list = []
    ci1 = round((ci_mean + 1.96(s_dev / square(len(set)))), 4)
    ci2 = round((ci_mean - 1.96(s_dev / square(len(set)))), 4)
    ci_list.append(ci1)
    ci_list.append(ci2)
    return ci_list
