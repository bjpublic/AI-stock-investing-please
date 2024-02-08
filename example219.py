from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

for i in range(1, 101):
    knn = KNeighborsRegressor(n_neighbors=i)
    knn.fit(train_scaled, train_target)
    score = knn.score(test_scaled, test_target)
    print("이웃 수: {} // 평가 점수: {}".format(i, score))
