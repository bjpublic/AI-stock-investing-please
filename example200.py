def get_balance(self):
    self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_number)
    self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
    self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "1")
    self.dynamicCall("CommRqData(QString, QString, int, QString)", "opw00018", "opw00018", 0, "0002")
    self.tr_event_loop.exec_()
    return self.tr_data
