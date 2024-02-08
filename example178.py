def _on_receive_tr_data(self, screen_no, rqname, trcode, record_name, next, v1, v2, v3, v4):
    print(screen_no, rqname, trcode, record_name, next)
    cnt = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)

    if next == "2":
        self.isnext = True
    else:
        self.isnext = False

    if rqname == "opt10081":
        total = []
        for i in range(cnt):
            date = self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "일자").strip()
            open = int(self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "시가").strip())
            high = int(self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "고가").strip())
            low = int(self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "저가").strip())
            close = int(self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "현재가").strip())
            volume = int(self.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, i, "거래량").strip())
            total.append([date, open, high, low, close, volume])
        self.tr_data = total

    self.tr_event_loop.exit()
    time.sleep(1)
