import csv
import pandas as pd

df = pd.read_csv('Log.csv',
                 index_col='Description',
                 names=['Description', 'User', 'Date and time', 'Hash'],
                 header=0)

print(df)

