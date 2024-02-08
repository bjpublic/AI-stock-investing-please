app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

print(kospi_list)
print(kosdaq_list)

print(len(kospi_list))
print(len(kosdaq_list))

app.exec_()