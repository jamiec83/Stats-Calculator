import pandas as pd

def meandev(data):
    series = pd.Series(data)

    result = series.mad()
    return result