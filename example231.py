app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")
kospi_dic = {}
kosdaq_dic = {}

for i in kospi_list:
    name = kiwoom.get_code_name(i)
    kospi_dic[i] = name

for i in kosdaq_list:
    name = kiwoom.get_code_name(i)
    kosdaq_dic[i] = name

print(kospi_dic)
print(kosdaq_dic)

app.exec_()
