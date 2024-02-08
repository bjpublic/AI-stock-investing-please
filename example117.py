import pandas as pd

df1 = pd.read_csv("concat_1.csv")
df2 = pd.read_csv("concat_2.csv")
df3 = pd.read_csv("concat_3.csv")

result = pd.concat([df1, df2, df3], ignore_index = True, axis = 1)
print(result)