def predict_stock(self, code):
    # 종목 코드를 가져와서 해당 종목의 모든 주식 가격 데이터 가져와서 데이터 프레임으로 만들기
    df = self.get_price(code)

    data = []
    target = []

    # 특정일의 주식 가격은 data, 특정일 다음날의 종가 가격은 target에 할당
    for i in range(len(df) - 1):
        a = list(df.iloc[i])
        b = df.iloc[i + 1, 3]
        data.append(a)
        target.append(b)

    data = np.array(data)
    target = np.array(target)

    # 랜덤 포레스트 머신러닝 모델 활용
    rf = RandomForestRegressor(oob_score=True)
    # 모델 학습
    rf.fit(data, target)

    # 현재 날짜의 주식 가격을 today_price 변수에 할당
    today_price = list(df.iloc[-1])

    # 현재 날짜의 가격을 통해 다음날 종가 예측
    predict_price = round(int(rf.predict([today_price])[0]), -2)

    # 예측한 가격이 현재 날짜의 종가보다 높을 경우 추천하는 글 화면에 출력
    if df.iloc[-1]['close'] < predict_price:
        name = self.get_code_name(code)
        print("{} 주가: {}원 -> 예측 {}원으로 추천합니다.".format(name, df.iloc[-1]['close'], predict_price))
