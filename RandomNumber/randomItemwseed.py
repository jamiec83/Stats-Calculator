from random import choice
from random import seed

def itemlistwseed(values):
    seed(1)
    values = ["Red","Blue", "Green","Yellow","Orange"]
    return choice(values)