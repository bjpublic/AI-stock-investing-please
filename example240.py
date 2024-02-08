app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

# 코스피, 코스닥 데이터가 저장될 딕셔너리 준비
kospi_dic = {}
kosdaq_dic = {}

deposit = kiwoom.get_deposit()
print("남은예수금: {}".format(deposit))
print("현재가지고있는종목: {}".format(kiwoom.get_balance()))

f = open("best.dat", 'rb')
kiwoom.best = pickle.load(f)
f.close()

for i in kiwoom.get_balance():
    if i[1] in kiwoom.best.keys():
        kiwoom.send_order("sell", "0001", 2, i[0][1:], kiwoom.best[i[0][1:]], "00")

# 코스피 종목 코드를 활용한 코스피 종목명 가져오기
for i in kospi_list:
    try:
        kospi_dic[i] = kiwoom.get_code_name(i)
        # 코스피 주가 예측
        kiwoom.predict_stock(i)
    except:
        continue

# 코스닥 종목 코드를 활용한 코스닥 종목명 가져오기
for i in kosdaq_list:
    try:
        kospi_dic[i] = kiwoom.get_code_name(i)
        # 코스닥 주가 예측
        kiwoom.predict_stock(i)
    except:
        continue

app.exec_()
