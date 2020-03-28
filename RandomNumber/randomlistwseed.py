from random import seed
from random import randint

def randomlist(num):
    seed(1)

    num = 10
    start = 10
    end = 20

    res = []
    for j in range(num):
        res.append(randint(start, end))


    return res