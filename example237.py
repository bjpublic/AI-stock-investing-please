app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

my_deposit = kiwoom.get_deposit()
print("나의예수금:", my_deposit)

kospi_dic = {}
kosdaq_dic = {}

for i in kospi_list:
    try:
        kospi_dic[i] = kiwoom.get_code_name(i)
        kiwoom.predict_stock(i)
    except:
        continue

for i in kosdaq_list:
    try:
        kosdaq_dic[i] = kiwoom.get_code_name(i)
        kiwoom.predict_stock(i)
    except:
        continue

app.exec_()
