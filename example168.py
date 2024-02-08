def get_code_list_stock_market(self, market_type):
    code_list = self.dynamicCall("GetCodeListByMarket(QString)", market_type)
    code_list = code_list.split(';')[:-1]
    return code_list
