def _on_receive_real_data(self, s_code, real_type, real_data):
    if real_type == "장시작시간":
        pass
    elif real_type == "주식체결":
        signed_at = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("체결시간"))
        close = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("현재가"))
        close = abs(int(close))

        high = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("고가"))
        high = abs(int(high))

        open = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("시가"))
        open = abs(int(open))

        low = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("저가"))
        low = abs(int(low))

        top_priority_ask = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("(최우선)매도호가"))
        top_priority_ask = abs(int(top_priority_ask))

        top_priority_bid = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("(최우선)매수호가"))
        top_priority_bid = abs(int(top_priority_bid))

        accum_volume = self.dynamicCall("GetCommRealData(QString, int)", s_code, get_fid("누적거래량"))
        accum_volume = abs(int(accum_volume))

        self.universe_realtime_transaction_info.append([s_code, signed_at, close, high, open, low, top_priority_ask, top_priority_bid, accum_volume])
        print(s_code, open, high, low, close, top_priority_ask, top_priority_bid, accum_volume)
