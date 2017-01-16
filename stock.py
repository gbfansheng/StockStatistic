# -*- coding: utf-8 -*-
import pandas as pd
import tushare as ts

# df = ts.get_today_all()
# codeDF = df['code']
# print(codeDF)
# codeDF.to_csv('today.csv',sep=',', encoding='utf-8')

readCodeDF = pd.read_csv('today.csv',sep=',', encoding='utf-8', dtype = str)
print(readCodeDF)