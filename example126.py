import pandas as pd

df = pd.read_csv("country_timeseries.csv")
print(df.fillna(0).iloc[:5, :5])