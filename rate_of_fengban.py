# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import datetime
import stock
import zhangting
import fengban_rate

def save_dict():
    global fengban_open_rou_dict, fengban_high_rou_dict, fengban_close_rou_dict, fengban_low_rou_dict
    global wunao_open_rou_dict, wunao_high_rou_dict, wunao_close_rou_dict, wunao_low_rou_dict
    global lanban_open_rou_dict, lanban_high_rou_dict, lanban_close_rou_dict, lanban_low_rou_dict

    f = open(stock.get_data_path() + 'open_rate', 'w')
    pickle.dump(fengban_open_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'high_rate', 'w')
    pickle.dump(fengban_high_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'close_rate', 'w')
    pickle.dump(fengban_close_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'low_rate', 'w')
    pickle.dump(fengban_low_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'wunao_open_rate', 'w')
    pickle.dump(wunao_open_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'wunao_high_rate', 'w')
    pickle.dump(wunao_high_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'wunao_close_rate', 'w')
    pickle.dump(wunao_close_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'wunao_low_rate', 'w')
    pickle.dump(wunao_low_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'lanban_open_rate', 'w')
    pickle.dump(wunao_open_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'lanban_high_rate', 'w')
    pickle.dump(wunao_high_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'lanban_close_rate', 'w')
    pickle.dump(wunao_close_rou_dict, f)
    f.close()

    f = open(stock.get_data_path() + 'lanban_low_rate', 'w')
    pickle.dump(wunao_low_rou_dict, f)
    f.close()
    # print fengban_open_rou_dict
    # print fengban_high_rou_dict
    # print fengban_close_rou_dict
    # print fengban_low_rou_dict
    # print wunao_open_rou_dict
    # print wunao_high_rou_dict
    # print wunao_close_rou_dict
    # print wunao_low_rou_dict


def get_open_rate_dict():
    f = open(stock.get_data_path() + 'open_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_high_rate_dict():
    f = open(stock.get_data_path() + 'high_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_close_rate_dict():
    f = open(stock.get_data_path() + 'close_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_low_rate_dict():
    f = open(stock.get_data_path() + 'low_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_wunao_open_rate_dict():
    f = open(stock.get_data_path() + 'wunao_open_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_wunao_high_rate_dict():
    f = open(stock.get_data_path() + 'wunao_high_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_wunao_close_rate_dict():
    f = open(stock.get_data_path() + 'wunao_close_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_wunao_low_rate_dict():
    f = open(stock.get_data_path() + 'wunao_low_rate', 'r')
    dict = pickle.load(f)
    return dict

def get_lanban_open_rate_dict():
    f = open(stock.get_data_path() + 'lanban_open_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_lanban_high_rate_dict():
    f = open(stock.get_data_path() + 'lanban_high_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_lanban_close_rate_dict():
    f = open(stock.get_data_path() + 'lanban_close_rate', 'r')
    dict = pickle.load(f)
    return dict


def get_lanban_low_rate_dict():
    f = open(stock.get_data_path() + 'lanban_low_rate', 'r')
    dict = pickle.load(f)
    return dict



def caculate_rou():
    fengban_dict = zhangting.get_fengban_dict()
    notfeng_dict = zhangting.get_notfeng_dict()
    global fengban_open_rou_dict, fengban_high_rou_dict, fengban_close_rou_dict, fengban_low_rou_dict
    global wunao_open_rou_dict, wunao_high_rou_dict, wunao_close_rou_dict, wunao_low_rou_dict
    global lanban_open_rou_dict, lanban_high_rou_dict, lanban_close_rou_dict, lanban_low_rou_dict
    fengban_open_rou_dict = {}
    fengban_high_rou_dict = {}
    fengban_close_rou_dict = {}
    fengban_low_rou_dict = {}
    wunao_open_rou_dict = {}
    wunao_high_rou_dict = {}
    wunao_close_rou_dict = {}
    wunao_low_rou_dict = {}
    lanban_open_rou_dict = {}
    lanban_high_rou_dict = {}
    lanban_close_rou_dict = {}
    lanban_low_rou_dict = {}

    for key in zhangting.get_fengban_dict():
        print key
        high_rate_list = []
        open_rate_list = []
        close_rate_list = []
        low_rate_list = []

        wunao_open_rate_list = []
        wunao_high_rate_list = []
        wunao_close_rate_list = []
        wunao_low_rate_list = []

        lanban_open_rate_list = []
        lanban_high_rate_list = []
        lanban_close_rate_list = []
        lanban_low_rate_list = []

        fengban_list = fengban_dict[key]
        for code in fengban_list:
            df = stock.read(code)
            zhangting_day = datetime.datetime.strptime(key, '%Y-%m-%d')
            after_zhangting_day = zhangting_day + datetime.timedelta(days=1)
            zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
            after_zhangting_daystring = after_zhangting_day.strftime('%Y-%m-%d')

            df_zhangting_day = df[df['date'].isin([zhangting_daystring])]
            df_after_zhangting_day = df[df['date'].isin([after_zhangting_daystring])]
            if df_after_zhangting_day.empty:
                end = datetime.datetime.now()
                for i in range((end - zhangting_day).days + 1):
                    after_zhangting_day = zhangting_day + datetime.timedelta(days=(i + 1))
                    after_zhangting_daystring = after_zhangting_day.strftime('%Y-%m-%d')
                    df_after_zhangting_day = df[df['date'].isin([after_zhangting_daystring])]
                    if not df_after_zhangting_day.empty:
                        break

            if not df_after_zhangting_day.empty and not df_zhangting_day.empty:
                high = float(df_zhangting_day['high'])
                after_open = float(df_after_zhangting_day['open'])
                after_high = float(df_after_zhangting_day['high'])
                after_close = float(df_after_zhangting_day['close'])
                after_low = float(df_after_zhangting_day['low'])

                open_rate = after_open / high - 1
                high_rate = after_high / high - 1
                close_rate = after_close / high - 1
                low_rate = after_low / high - 1

                open_rate_list.append(open_rate)
                high_rate_list.append(high_rate)
                close_rate_list.append(close_rate)
                low_rate_list.append(low_rate)

        if len(open_rate_list) > 0 :
            open_rate = sum(open_rate_list) / float(len(open_rate_list))
            high_rate = sum(high_rate_list) / float(len(high_rate_list))
            close_rate = sum(close_rate_list) / float(len(close_rate_list))
            low_rate = sum(low_rate_list) / float(len(low_rate_list))
            fengban_open_rou_dict[key] = open_rate
            fengban_high_rou_dict[key] = high_rate
            fengban_close_rou_dict[key] = close_rate
            fengban_low_rou_dict[key] = low_rate

        notfeng_list = notfeng_dict.get(key, [])
        wunao_open_rate_list.extend(open_rate_list)
        wunao_high_rate_list.extend(high_rate_list)
        wunao_close_rate_list.extend(close_rate_list)
        wunao_low_rate_list.extend(low_rate_list)

        for code in notfeng_list:
            df = stock.read(code)
            zhangting_day = datetime.datetime.strptime(key, '%Y-%m-%d')
            after_zhangting_day = zhangting_day + datetime.timedelta(days=1)
            zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
            after_zhangting_daystring = after_zhangting_day.strftime('%Y-%m-%d')

            df_zhangting_day = df[df['date'].isin([zhangting_daystring])]
            df_after_zhangting_day = df[df['date'].isin([after_zhangting_daystring])]

            if df_after_zhangting_day.empty:
                end = datetime.datetime.now()
                for i in range((end - zhangting_day).days + 1):
                    after_zhangting_day = zhangting_day + datetime.timedelta(days=(i + 1))
                    after_zhangting_daystring = after_zhangting_day.strftime('%Y-%m-%d')
                    df_after_zhangting_day = df[df['date'].isin([after_zhangting_daystring])]
                    if not df_after_zhangting_day.empty:
                        break

            if not df_after_zhangting_day.empty and not df_zhangting_day.empty:
                high = float(df_zhangting_day['high'])
                after_open = float(df_after_zhangting_day['open'])
                after_high = float(df_after_zhangting_day['high'])
                after_close = float(df_after_zhangting_day['close'])
                after_low = float(df_after_zhangting_day['low'])

                open_rate = after_open / high - 1
                high_rate = after_high / high - 1
                close_rate = after_close / high - 1
                low_rate = after_low / high - 1

                wunao_open_rate_list.append(open_rate)
                wunao_high_rate_list.append(high_rate)
                wunao_close_rate_list.append(close_rate)
                wunao_low_rate_list.append(low_rate)

                lanban_open_rate_list.append(open_rate)
                lanban_high_rate_list.append(high_rate)
                lanban_close_rate_list.append(close_rate)
                lanban_low_rate_list.append(low_rate)

        if len(wunao_open_rate_list) > 0:
            wunao_open_rate = sum(wunao_open_rate_list) / len(wunao_open_rate_list)
            wunao_high_rate = sum(wunao_high_rate_list) / len(wunao_high_rate_list)
            wunao_close_rate = sum(wunao_close_rate_list) / len(wunao_close_rate_list)
            wunao_low_rate = sum(wunao_low_rate_list) / len(wunao_low_rate_list)

            wunao_open_rou_dict[key] = wunao_open_rate
            wunao_high_rou_dict[key] = wunao_high_rate
            wunao_close_rou_dict[key] = wunao_close_rate
            wunao_low_rou_dict[key] = wunao_low_rate


        if len(lanban_open_rate_list) > 0:

            lanban_open_rate = sum(lanban_open_rate_list) / len(lanban_open_rate_list)
            lanban_high_rate = sum(lanban_high_rate_list) / len(lanban_high_rate_list)
            lanban_close_rate = sum(lanban_close_rate_list) / len(lanban_close_rate_list)
            lanban_low_rate = sum(lanban_low_rate_list) / len(lanban_low_rate_list)

            lanban_open_rou_dict[key] = lanban_open_rate
            lanban_high_rou_dict[key] = lanban_high_rate
            lanban_close_rou_dict[key] = lanban_close_rate
            lanban_low_rou_dict[key] = lanban_low_rate

def rate_of_all():
    print 'start'
    zhangting_rate_dict = fengban_rate.read_zhangting_rate_dict()
    fengban_dict = zhangting.get_fengban_dict()
    notfeng_dict = zhangting.get_notfeng_dict()

    open_rate_dict = get_open_rate_dict()
    high_rate_dict = get_high_rate_dict()
    close_rate_dict = get_close_rate_dict()
    low_rate_dict = get_low_rate_dict()

    wunao_open_rate_dict = get_wunao_open_rate_dict()
    wunao_high_rate_dict = get_wunao_high_rate_dict()
    wunao_close_rate_dict = get_wunao_close_rate_dict()
    wunao_low_rate_dict = get_wunao_low_rate_dict()

    lanban_open_rate_dict = get_lanban_open_rate_dict()
    lanban_high_rate_dict = get_lanban_high_rate_dict()
    lanban_close_rate_dict = get_lanban_close_rate_dict()
    lanban_low_rate_dict = get_lanban_low_rate_dict()

    date_list = []
    fengban_count_list = []
    notfengban_count_list = []
    fengban_rate_list = []
    open_rate_list = []
    high_rate_list = []
    close_rate_list = []
    low_rate_list = []
    wunao_open_rate_list = []
    wunao_high_rate_list = []
    wunao_close_rate_list = []
    wunao_low_rate_list = []
    lanban_open_rate_list = []
    lanban_high_rate_list = []
    lanban_close_rate_list = []
    lanban_low_rate_list = []

    for key in zhangting_rate_dict:
        fengban_list = fengban_dict.get(key, [])
        notfeng_list = notfeng_dict.get(key, [])
        fengban_count_list.append(len(fengban_list))
        notfengban_count_list.append(len(notfeng_list))
        fengban_rate_list.append(zhangting_rate_dict[key])
        date_list.append(key)
        open_rate_list.append(open_rate_dict.get(key , ''))
        high_rate_list.append(high_rate_dict.get(key , ''))
        close_rate_list.append(close_rate_dict.get(key , ''))
        low_rate_list.append(low_rate_dict.get(key , ''))

        wunao_open_rate_list.append(wunao_open_rate_dict.get(key , ''))
        wunao_high_rate_list.append(wunao_high_rate_dict.get(key , ''))
        wunao_close_rate_list.append(wunao_close_rate_dict.get(key , ''))
        wunao_low_rate_list.append(wunao_low_rate_dict.get(key , ''))

        lanban_open_rate_list.append(lanban_open_rate_dict.get(key , ''))
        lanban_high_rate_list.append(lanban_high_rate_dict.get(key , ''))
        lanban_close_rate_list.append(lanban_close_rate_dict.get(key , ''))
        lanban_low_rate_list.append(lanban_low_rate_dict.get(key , ''))

    df = pd.DataFrame({'date' : date_list , '封板数' : fengban_count_list, '未封数' : notfengban_count_list, '封板率' : fengban_rate_list,
                       '竞价肉' : open_rate_list, '最高价肉' : high_rate_list, '收盘肉' : close_rate_list, '最低价肉' : low_rate_list,
                       '无脑板竞价肉' : wunao_open_rate_list, '无脑板最高价肉' : wunao_high_rate_list, '无脑板收盘肉' : wunao_close_rate_list
                       , '无脑板最低价肉' : wunao_low_rate_list,'烂板竞价肉' : lanban_open_rate_list, '烂板最高价肉' : lanban_high_rate_list, '烂板收盘肉' : lanban_close_rate_list
                       , '烂板最低价肉' : lanban_low_rate_list} ,
                      columns=['date', '封板数' , '未封数' , '封板率' , '竞价肉' , '最高价肉' , '收盘肉' , '最低价肉' ,'无脑板竞价肉' , '无脑板最高价肉' , '无脑板收盘肉', '无脑板最低价肉','烂板竞价肉' , '烂板最高价肉' , '烂板收盘肉'
                       , '烂板最低价肉' ])
    df = df.sort_values(by = 'date')
    print (df)
    stock.save(df, 'rate_of_all')


if __name__ == '__main__':
    caculate_rou()
    save_dict()
    rate_of_all()