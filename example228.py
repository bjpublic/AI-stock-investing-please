rf = RandomForestRegressor(oob_score=True)
rf.fit(전체 데이터 문제집, 전체 데이터 정답지)
score = rf.oob_score_
print("평가 점수: {}".format(score))
