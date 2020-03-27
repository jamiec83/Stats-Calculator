from Calculator.SquareRoot import squareroot
from Statistics.Variance import variance


def sd(num):
    try:
        variance_float = variance(num)
        return round(squareroot(variance_float), 2)
    except ZeroDivisionError:
        print("Watch out: You're dividing by Zero!")


