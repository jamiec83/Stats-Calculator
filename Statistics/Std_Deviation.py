from Calculator.SquareRoot import squareroot
from Statistics.Variance import variance


def sdeviation(num):
    try:
        variance_float = variance(num)
        return round(squareroot(variance_float), 5)
    except ZeroDivisionError:
        print("Watch out: You're dividing by Zero!")


