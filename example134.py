import pandas as pd

df = pd.read_csv("country_timeseries.csv")
idx = df[df['Day'] > 100].index
print(df.drop(idx).iloc[:, :3])