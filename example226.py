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

best = 0
for n in range(1, 101):
    dt = DecisionTreeRegressor(max_depth=n)
    dt.fit(train_input, train_target)
    score = dt.score(test_input, test_target)
    if score > best:
        best = score
        best_n = n

dt = DecisionTreeRegressor(max_depth=best_n)
dt.fit(train_input, train_target)
score = dt.score(test_input, test_target)

new = [61800, 62400, 61400, 61800, 12236503]

pred = dt.predict([new])
print("내일 2022년 11월 21일 삼성전자 주식 가격의 종가는 {}원 입니다.".format(pred[0]))
