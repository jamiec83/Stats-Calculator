import numpy as np


def sys_sample(df, r, n):
    data = np.array([25, 15, 20, 25, 18, 12, 24, 30, 15, 20, 10, 10, 11, 14, 22, 16])
    k = df.shape[0] / n
    b = [None] * n
    a = r
    b[0] = a
    for i in np.arange(1, n):
        a = a + k
        if a > df.shape[0]:
            a = a - df.shape[0]
        b[i] = a
    return {"Data": df[b], "Index": b, "K": k}
