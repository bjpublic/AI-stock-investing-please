app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

my_deposit = kiwoom.get_deposit()
print("나의예수금:", my_deposit)
order_samsung = kiwoom.send_order("buy", "0001", 1, "005930", 1, 60400, "00")
print(order_samsung)

app.exec_()