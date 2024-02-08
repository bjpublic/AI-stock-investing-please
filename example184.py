def get_deposit(self):
    self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.ac_count_number)
    self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
    self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "2")
    self.dynamicCall("CommRqData(QString, QString, int, QString)", "opw00001", "opw00001", 0, "0002")
    self.tr_event_loop.exec_()
    return self.tr_data
