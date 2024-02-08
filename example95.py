import pandas as pd

date = ['2022/11/07', '2022/11/08', '2022/11/09', '2022/11/10', '2022/11/11']
date = pd.to_datetime(date, format = '%Y/%m/%d')

price = [60300, 61900, 62200, 61500, 63200]

samsung = pd.Series(price, index=date)
print(samsung)