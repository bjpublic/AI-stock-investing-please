def get_order(self):
    self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_number)
    self.dynamicCall("SetInputValue(QString, QString)", "전체종목구분", "0")
    self.dynamicCall("SetInputValue(QString, QString)", "체결구분", "0")
    self.dynamicCall("SetInputValue(QString, QString)", "매매구분", "0")
    self.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10075", "opt10075", 0, "0002")
    self.tr_event_loop.exec_()
    return self.tr_data
