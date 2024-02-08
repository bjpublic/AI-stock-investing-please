import pandas as pd

df = pd.read_csv("country_timeseries.csv")
print(df.iloc[:5, :5])