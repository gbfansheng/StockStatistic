# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import datetime
import stock
import zhangting


def caculate_fengban_rate():
    global zhangting_rate_dict
    zhangting_rate_dict = {}
    zhangting_dict = zhangting.get_fengban_dict()
    notfeng_dict = zhangting.get_notfeng_dict()

    begin = zhangting.begin_date()
    end = datetime.datetime.now().date()
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        daystring = day.strftime('%Y-%m-%d')
        zhangting_list = zhangting_dict.get(daystring,[])
        notzhangting_list = notfeng_dict.get(daystring,[])
        zhangting_count = len(zhangting_list)
        notzhangting_count = len(notzhangting_list)

        if zhangting_count > 0 or notzhangting_count > 0 :
            zhangting_rate = zhangting_count / float(zhangting_count + notzhangting_count)
            zhangting_rate_dict[daystring] = zhangting_rate


def save_zhangting_rate():
    global zhangting_rate_dict
    f = open(stock.get_data_path() + 'zhangting_rate', 'w')
    pickle.dump(zhangting_rate_dict, f)
    f.close()
    print (zhangting_rate_dict)


def read_zhangting_rate_dict():
    f = open(stock.get_data_path() + 'zhangting_rate', 'r')
    return pickle.load(f)







if __name__ == '__main__':
    caculate_fengban_rate()
    save_zhangting_rate()