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
    begin = begin_date()
    end = datetime.datetime.now().date()
    for i in range((end - begin).days + 1):
        zhangting_day = begin + datetime.timedelta(days=i)
        before_zhangting_day = zhangting_day - datetime.timedelta(days=1)
        zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
        before_zhangting_daystring = before_zhangting_day.strftime('%Y-%m-%d')
        df_zhangting_day = df[df['date'].isin([zhangting_daystring])]
        df_before_zhangting_day = df[df['date'].isin([before_zhangting_daystring])]
        fengban_list = fengban_dict.get(zhangting_daystring, [])
        notfeng_list = notfeng_dict.get(zhangting_daystring, [])

        if df_before_zhangting_day.empty:
            for i in range(10):
                before_zhangting_day = zhangting_day - datetime.timedelta(days=i + 1)
                before_zhangting_daystring = before_zhangting_day.strftime('%Y-%m-%d')
                df_before_zhangting_day = df[df['date'].isin([before_zhangting_daystring])]
                if not df_before_zhangting_day.empty:
                    break

        # 当天有数据
        if not df_zhangting_day.empty and not df_before_zhangting_day.empty:
            p_change = float(df_zhangting_day['p_change'])
            high = float(df_zhangting_day['high'])
            close = float(df_zhangting_day['close'])
            low = float(df_zhangting_day['low'])
            base_price = float(df_before_zhangting_day['close'])
            turnover = float(df_zhangting_day['turnover'])
            if p_change >= 9.9 and p_change < 11 and high == close and turnover > 10:
                # 如果涨停则保存
                fengban_list.append(code)
                fengban_dict[zhangting_daystring] = fengban_list
            else:
                if p_change >= 9.9 and p_change < 11 and high == close and high != low:
                    # 如果涨停则保存
                    fengban_list.append(code)
                    fengban_dict[zhangting_daystring] = fengban_list

            if (high / base_price) >= 1.099 and high != close and turnover > 0.1:
                # 冲板未封
                notfeng_list.append(code)
                notfeng_dict[zhangting_daystring] = notfeng_list


def begin_date():
    return datetime.date(2016, 11, 1);


# def saveDict():
#     global fengban_dict
#     global notfeng_dict
#     f = open(stock.get_data_path() + 'zhangting', 'w')
#     pickle.dump(fengban_dict, f)
#     f.close()
#     f = open(stock.get_data_path() + 'notfeng', 'w')
#     pickle.dump(notfeng_dict, f)
#     f.close()


def get_fengban_dict():
    return stock.get_dict('zhangting')


def get_notfeng_dict():
    return stock.get_dict('notfeng')


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
    stock.save_dict(fengban_dict, 'zhangting')
    stock.save_dict(notfeng_dict, 'notfeng')

if __name__ == '__main__':
    zhangting()