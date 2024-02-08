from sklearn.ensemble import RandomForestRegressor
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

rf = RandomForestRegressor(oob_score=True)
rf.fit(data, target)
score = rf.oob_score_
print("평가 점수: {}".format(score))

new = [61800, 62400, 61400, 61800, 12236503]

pred = rf.predict([new])
print("내일 2022년 11월 21일 삼성전자 주식 가격의 종가는 {}원입니다.".format(pred[0]))
