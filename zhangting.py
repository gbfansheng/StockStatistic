# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import stock
import datetime
import os
import stock

def processDf(code, df):
    global dateDict
    begin = datetime.date(2016, 12, 30)
    end = datetime.datetime.now().date()
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        daystring = day.strftime('%Y-%m-%d')
        dfForDay = df[df['date'].isin([daystring])]
        datelist = dateDict.get(daystring, [])

        # 当天有数据
        if not dfForDay.empty:
            p_change = float(dfForDay['p_change'])
            high = float(dfForDay['high'])
            close = float(dfForDay['close'])
            turnover = float(dfForDay['turnover'])
            if p_change > 9.9 and p_change < 11 and high == close and turnover > 3.0:
                # 如果涨停则保存
                datelist.append(code)
                dateDict[daystring] = datelist


def saveDict():
    global dateDict
    f = open(stock.get_data_path() + 'zhangting','w')
    pickle.dump(dateDict,f)
    f.close()


def getDict():
    f = open(stock.get_data_path() + 'zhangting','r')
    dateDict = pickle.load(f)
    return dateDict


def zhangting():
    global dateDict
    dateDict = {}
    todayDF = stock.get_today()
    codeList = list(todayDF['code'])
    for code in codeList:
        print (code)
        codeDF = stock.read(code)
        # 文件是否存在
        if codeDF is None:
            pass
        else:
            processDf(code, codeDF)
    saveDict()



if __name__ == '__main__':
    zhangting()
    getDict()
