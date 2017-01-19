# -*- coding: utf-8 -*-

import pandas as pd
import tushare as ts
import os
import datetime


def downloadToday():
    df = ts.get_today_all()
    df.to_csv('today.csv', sep=',', encoding='utf-8')
    pass


def get_today():
    todayDf = pd.read_csv('today.csv', sep=',', encoding='utf-8', dtype=str)
    return todayDf


def get_data_path():
    parent = os.path.dirname(os.getcwd())
    data_path = parent + '/data/'
    if not os.path.exists(data_path) :
        os.makedirs(data_path)
    return data_path

def read(code):
    fileName = code + '.csv'
    # 文件是否存在
    if os.path.isfile(get_data_path() + fileName):
        df = pd.read_csv(get_data_path() + fileName, sep=',', encoding='utf-8', dtype=str)
        return df
    else:
        return None


def save(df, code):
    fileName = code + '.csv'
    df.to_csv(get_data_path() + fileName)


def downloadHistory():
    todayDF = get_today()
    codeList = list(todayDF['code'])
    for code in codeList:
        codeDF = read(code)
        if codeDF is None:
            print('downloading ' + code)
            df = ts.get_hist_data(code)
            if df is None:
                pass
            else:
                # 新股没有数据，return none
                save(df, code)
        else:
            ##处理时间
            dateList = list(codeDF['date'])
            dateString = dateList[0:1][0]
            nowdt = datetime.datetime.now()
            nowdtstring = nowdt.strftime('%Y-%m-%d')
            if dateString == nowdtstring:
                pass
            else:
                ##获取两日日期之间的数据
                dt = datetime.datetime.strptime(dateString, '%Y-%m-%d')
                dt = dt + datetime.timedelta(days=1)
                dtstring = dt.strftime('%Y-%m-%d')
                additionDF = ts.get_hist_data(code=code, start=dtstring, end=nowdtstring)
                concatDF = additionDF.append(codeDF)
                save(concatDF, code)


if __name__ == '__main__':
    downloadToday()
    downloadHistory()
