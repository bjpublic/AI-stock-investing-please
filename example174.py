def _set_signal_slots(self):
    self.OnEventConnect.connect(self._login_slot)
    self.OnReceiveTrData.connect(self._on_receive_tr_data)
