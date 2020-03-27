# Import numpy library
import numpy as np


def quartiles(data):
    Q1 = np.percentile(data, 25)
    Q2 = np.percentile(data,50)
    Q3 = np.percentile(data, 75)
    Q4 = np.percentile(data, 100)
    Quarts = Q1, Q2, Q3, Q4
    return Quarts
