def _set_signal_slots(self):
    self.OnEventConnect.connect(self._login_slot)
    self.OnReceiveTrData.connect(self._on_receive_tr_data)
    self.OnReceiveMsg.connect(self._on_receive_msg)
    self.OnReceiveChejanData.connect(self._on_chejan_slot)
    self.OnReceiveRealData.connect(self._on_receive_real_data)
