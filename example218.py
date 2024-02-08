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

knn = KNeighborsRegressor()
knn.fit(train_scaled, train_target)

new = [61800, 62400, 61400, 61800, 12236503]

new2 = ss.transform([new])
pred = knn.predict(new2)

print("내일 2022년 11월 21일의 삼성전자 주식 가격의 종가는 {}원입니다.".format(pred[0]))
