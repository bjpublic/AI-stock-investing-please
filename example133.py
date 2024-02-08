import pandas as pd

df = pd.read_csv("country_timeseries.csv")
print(df.dropna())