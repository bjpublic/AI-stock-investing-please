from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import pandas as pd

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._make_kiwoom_instance()
        self._set_signal_slots()
        self._comm_connect()
        self.account_number = self.get_account_number()

    def _make_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._login_slot)

    def _login_slot(self, err_code):
        if err_code == 0:
            print("Connected!")
        else:
            print("Not Connected...")
        self.login_event_loop.exit()

    def _comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def get_account_number(self):
        account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCLIST")
        account_number = account_list.split(';')[0]
        print("나의계좌번호:", account_number)
        return account_number

app = QApplication(sys.argv)
kiwoom = Kiwoom()
kiwoom.get_account_number()
app.exec_()
