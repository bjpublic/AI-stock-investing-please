def set_real_reg(self, str_screen_no, str_code_list, str_fid_list, str_opt_type):
    self.dynamicCall("SetRealReg(QString, QString, QString, QString)", str_screen_no, str_code_list, str_fid_list, str_opt_type)
    time.sleep(1)
