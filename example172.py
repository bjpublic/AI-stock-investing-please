app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

for i in kospi_list:
    name = kiwoom.get_code_name(i)
    print(i, name)

for i in kosdaq_list:
    name = kiwoom.get_code_name(i)
    print(i, name)

app.exec_()
