import pandas as pd
from numpy import nan

date = ['2022/12/01', '2022/12/02', '2022/12/09', '2022/12/10']
date = pd.to_datetime(date, format = '%Y/%m/%d')

values = [1, nan, nan, 10]

series = pd.Series(values, index = date)
series = series.interpolate(method='time')
print(series)