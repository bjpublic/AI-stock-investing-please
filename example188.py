def send_order(self, rqname, screen_no, order_type, code, order_quantity, order_price, order_gubun, order_no=""):
    order_result = self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                                    rqname, screen_no, self.account_number, order_type, code, order_quantity,
                                    order_price, order_gubun, order_no)
    return order_result
