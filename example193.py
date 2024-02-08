from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import pandas as pd

FID_CODES = {
    "10": "현재가",
    "11": "전일 대비",
    "12": "등락률",
    # ...중략...
    "9201": "계좌번호",
    "9203": "주문번호",
    "9205": "관리자사번"
}

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._make_kiwoom_instance()
        self._set_signal_slots()
        self._comm_connect()
        self.account_number = self.get_account_number()
        self.tr_event_loop = QEventLoop()
