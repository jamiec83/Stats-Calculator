from random import sample
from random import seed


def nlistw(n):
    seed (1)
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = sample(values, 5)
    return n
