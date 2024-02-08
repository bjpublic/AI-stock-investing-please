def get_price(self, code):
    self.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
    self.dynamicCall("SetInputValue(QString, QString)", "수정주가구분", "1")
    self.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10081", "opt10081", 0, "0020")
    self.tr_event_loop.exec_()
    time.sleep(1)

    total = self.tr_data

    while self.isnext:
        self.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        self.dynamicCall("SetInputValue(QString, QString)", "수정주가구분", "1")
        self.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10081", "opt10081", 2, "0020")
        self.tr_event_loop.exec_()
        total += self.tr_data
        time.sleep(1)

    df = pd.DataFrame(total, columns=['date', 'open', 'high', 'low', 'close', 'volume']).set_index("date")
    df = df.drop_duplicates()
    df = df.sort_index()
    return df
