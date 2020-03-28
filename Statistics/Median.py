from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def median(set):
    set = [1, 2, 3, 4, 5]
    n = len(set)
    set.sort()

    if n % 2 == 0:
        median1 = set[n // 2]
        median2 = set[n // 2 - 1]
        media = (median1 + median2) / 2
    else:
        media = set[n // 2]
    return media

