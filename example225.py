from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
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

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2)

for n in range(1, 11):
    dt = DecisionTreeRegressor(max_depth=n)
    dt.fit(train_input, train_target)
    score = dt.score(test_input, test_target)
    print("깊이: {} // 평가 점수: {}".format(n, score))
