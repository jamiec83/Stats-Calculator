from random import sample


def sys_sample(set):
    pop = range(1,100)
    k = 5
    result = sample(pop,k)
    return {"Data": pop, "K": k, "Result": result}
