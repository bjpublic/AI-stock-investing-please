def get_account_number(self):
    account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCLIST")
    account_number = account_list.split(';')[0]
    print("나의계좌번호:", account_number)
    return account_number
