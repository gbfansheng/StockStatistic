# -*- coding: utf-8 -*-

import pandas as pd
import tushare as ts
import os
import datetime
import pickle


def downloadToday():
    df = ts.get_today_all()
    df.to_csv('today.csv', sep=',', encoding='utf-8')
    code_list = df['code']
    name_list = df['name']
    name_dict = {}
    for i in range(len(code_list)):
        name_dict[code_list[i]] = name_list[i]
    save_dict(name_dict, 'name_dict')
    pass


def save_dict(dict, name):
    f = open(get_data_path() + name, 'w')
    pickle.dump(dict, f)
    f.close()


def get_name_dict():
    return get_dict('name_dict')


def get_dict(name):
    f = open(get_data_path() + name, 'r')
    dict = pickle.load(f)
    return dict


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


def read_code(code):
    fileName = code + '.csv'
    # 文件是否存在
    if os.path.isfile(get_data_path() + fileName):
        df = pd.read_csv(get_data_path() + fileName, sep=',', encoding='utf-8', dtype=str, index_col='date')
        return df
    else:
        return None


def save(df, name):
    fileName = name + '.csv'
    df.to_csv(get_data_path() + fileName)


def downloadHistory():
    todayDF = get_today()
    codeList = list(todayDF['code'])
    for code in codeList:
        print (code)
        codeDF = read_code(code)
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
            # dateList = list(codeDF.get('date'))
            # dateString = dateList[0:1][0]
            nowdt = datetime.datetime.now()
            nowdtstring = nowdt.strftime('%Y-%m-%d')
            indexs = list(codeDF.index)
            if indexs.__contains__(nowdtstring):
                pass
            else:
                ##获取两日日期之间的数据
                dateString = indexs[0]
                dt = datetime.datetime.strptime(dateString, '%Y-%m-%d')
                dt = dt + datetime.timedelta(days=1)
                dtstring = dt.strftime('%Y-%m-%d')
                additionDF = ts.get_hist_data(code=code, start=dtstring, end=nowdtstring)
                concatDF = pd.concat([additionDF, codeDF])
                save(concatDF, code)


if __name__ == '__main__':
    downloadToday()
    downloadHistory()
