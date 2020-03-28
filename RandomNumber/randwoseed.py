from random import randint
from random import randrange


def woseed(value):

    for _ in range(10):
        value = randint(0,10)
        value2 = float(randrange(0, 10))
        return value, value2