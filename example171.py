def get_code_name(self, code):
    name = self.dynamicCall("GetMasterCodeName(QString)", code)
    return name
