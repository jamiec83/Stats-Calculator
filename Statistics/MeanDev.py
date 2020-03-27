import pandas as pd
import numpy as np

def meandev(data):
    series = pd.Series(data)

    result = series.mad()
    return result