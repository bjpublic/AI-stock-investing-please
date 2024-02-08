from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np

samsung = pd.read_csv("full_samsung.csv", index_col="date")

data = []
target = []

for i in range(len(samsung) - 1):
    a = list(samsung.iloc[i])
    b = samsung.iloc[i+1, 3]
    data.append(a)
    target.append(b)

data = np.array(data)
target = np.array(target)

knn = KNeighborsRegressor()
knn.fit(data, target)
