import pandas as pd

# Creating a CSVReader using pandas and telling it to read from Skewness Unit test
data = pd.read_csv("Skewness.csv")

# telling pandas to find skewness for each row of data and to skip invalid data
df.skew(axis = 1, skipna = True)
