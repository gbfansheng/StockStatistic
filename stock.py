# -*- coding: utf-8 -*-
import pandas as pd
import tushare as ts

df = ts.get_today_all()
print(df)