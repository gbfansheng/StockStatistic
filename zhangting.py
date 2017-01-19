# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import stock
import datetime
import os
import stock


def processDf(code, df):
    global fengban_dict
    global notfeng_dict
    begin = datetime.date(2016, 10, 20)
    end = datetime.datetime.now().date()
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        daystring = day.strftime('%Y-%m-%d')
        dfForDay = df[df['date'].isin([daystring])]
        fengban_list = fengban_dict.get(daystring, [])
        notfeng_list = notfeng_list.get(daystring, [])

        # 当天有数据
        if not dfForDay.empty:
            p_change = float(dfForDay['p_change'])
            high = float(dfForDay['high'])
            close = float(dfForDay['close'])
            open = float(dfForDay['open'])
            turnover = float(dfForDay['turnover'])
            if p_change > 9.9 and p_change < 11 and high == close and turnover > 3.0:
                # 如果涨停则保存
                fengban_list.append(code)
                fengban_dict[daystring] = fengban_list

            if p_change < 9.9 and (high / open >= 9.9) and high != close and turnover > 3.0:
                # 冲板未封
                notfeng_list.append(code)
                notfeng_dict[daystring] = notfeng_list


def saveDict():
    global fengban_dict
    global notfeng_dict
    f = open(stock.get_data_path() + 'zhangting', 'w')
    pickle.dump(fengban_dict, f)
    f.close()
    f = open(stock.get_data_path() + 'notfeng', 'w')
    pickle.dump(notfeng_dict, f)
    f.close()


def get_fengban_dict():
    f = open(stock.get_data_path() + 'zhangting', 'r')
    dict = pickle.load(f)
    print ('fengban dict')
    print (dict)
    return dict

def get_notfeng_dict():
    f = open(stock.get_data_path() + 'notfeng', 'r')
    dict = pickle.load(f)
    print ('not feng')
    print (dict)
    return dict

def zhangting():
    global fengban_dict
    global notfeng_dict
    fengban_dict = {}
    notfeng_dict = {}
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
    get_fengban_dict()
    get_notfeng_dict()