app = QApplication(sys.argv)
kiwoom = Kiwoom()

# 코스피 주식 코드 가져오기
kospi_list = kiwoom.get_code_list_stock_market("0")
# 코스닥 주식 코드 가져오기
kosdaq_list = kiwoom.get_code_list_stock_market("10")

my_deposit = kiwoom.get_deposit()
print("나의예수금:", my_deposit)

fids = get_fid("체결시간")
codes = "005930;007700;000660;"
kiwoom.set_real_reg("0001", codes, fids, "0")

app.exec_()