def _on_receive_tr_data(self, screen_no, rqname, trcode, record_name, next, v1, v2, v3, v4):
    print(screen_no, rqname, trcode, record_name, next)
    cnt = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)

    if next == "2":
        self.isnext = True
    else:
        self.isnext = False
