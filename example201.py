elif rqname == "opw00018":
    box = []
    for i in range(cnt):
        code = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "종목번호")
        code_name = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "종목명")
        quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "보유수량")
        purchase_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "매입가")
        return_rate = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "수익률(%)")
        current_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "현재가")
        total_purchase_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "매입금액")
        available_quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "매매가능수량")

        code = code.strip()[1:]
        code_name = code_name.strip()
        quantity = int(quantity)
        purchase_price = int(purchase_price)
        return_rate = float(return_rate)
        current_price = int(current_price)
        total_purchase_price = int(total_purchase_price)
        available_quantity = int(available_quantity)

        box.append([code, code_name, quantity, purchase_price, return_rate, current_price, total_purchase_price, available_quantity])

    self.tr_data = box
