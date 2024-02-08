app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")
# 코스피, 코스닥 데이터가 저장될 딕셔너리 준비
kospi_dic = {}
kosdaq_dic = {}

# 코스피 종목 코드를 활용한 코스피 종목명 가져오기
for i in kospi_list:
    kospi_dic[i] = kiwoom.get_code_name(i)
    # 코스피 주가 예측
    kiwoom.predict_stock(i)

# 코스닥 종목 코드를 활용한 코스닥 종목명 가져오기
for i in kosdaq_list:
    kosdaq_dic[i] = kiwoom.get_code_name(i)
    # 코스피 주가 예측
    kiwoom.predict_stock(i)

app.exec_()
