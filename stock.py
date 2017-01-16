# -*- coding: utf-8 -*-
import pandas as pd
import tushare as ts

df = ts.get_today_all()
codeDF = df['code']
codeDF.to_csv('today.csv')