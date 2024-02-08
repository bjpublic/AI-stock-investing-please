def _on_receive_chejan(self, gubun, cnt, fid_list):
    print(gubun, cnt, fid_list)

    for fid in fid_list.split(";"):
        code = self.dynamicCall("GetChejanData(int)", "9001")[1:]
        data = self.dynamicCall("GetChejanData(int)", fid).lstrip("+").lstrip("-")
        if data.isdigit():
            data = int(data)
        name = FID_CODES[fid]
        print('{} : {}'.format(name, data))
