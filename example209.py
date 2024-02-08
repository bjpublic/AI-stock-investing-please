import pandas as pd

samsung = pd.read_csv("full_samsung.csv", index_col="date")
print(samsung)