elif rqname == "opt10075":
    box = []
    for i in range(cnt):
        code = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "종목코드")
        code_name = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "종목명")
        order_number = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "주문번호")
        order_status = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "주문상태")
        order_quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "주문수량")
        order_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "주문가격")
        current_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "현재가")
        order_type = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "주문구분")
        left_quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "미체결수량")
        executed_quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "체결량")
        ordered_at = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "시간")
        fee = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "당일매매수수료")
        tax = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "당일매매세금")

        code = code.strip()
        code_name = code_name.strip()
        order_number = str(int(order_number.strip()))
        order_status = order_status.strip()
        order_quantity = int(order_quantity.strip())
        order_price = int(order_price.strip())
        current_price = int(current_price.strip().lstrip("+").lstrip("-"))
        order_type = order_type.strip().lstrip("+").lstrip("-")
        left_quantity = int(left_quantity.strip())
        executed_quantity = int(executed_quantity.strip())
        ordered_at = ordered_at.strip()
        fee = int(fee)
        tax = int(tax)

        box.append([code, code_name, order_number, order_status, order_quantity, order_price, current_price, order_type, left_quantity, executed_quantity, ordered_at, fee, tax])

    self.tr_data = box

self.tr_event_loop.exit()
time.sleep(1)
