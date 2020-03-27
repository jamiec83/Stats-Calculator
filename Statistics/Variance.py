from Calculator.Square import square
from Calculator.Division import division
from Statistics.Mean import mean


def variance(num):
    try:
        mean_value = mean(num)
        num_value = len(num)
        x = 0
        for i in num:
            x = x + square(i - mean_value)
        return round(division(x, num_value),2)
    except ZeroDivisionError:
        print("Watch out: You're dividing by zero")

