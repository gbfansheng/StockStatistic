# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import datetime
import stock
import zhangting
import matplotlib.pyplot as plt
import matplotlib.dates


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


def fengban_df():
    zhangting_rate_dict = read_zhangting_rate_dict()
    fengban_dict = zhangting.get_fengban_dict()
    notfeng_dict = zhangting.get_notfeng_dict()
    df = pd.DataFrame(columns=['date', 'fengban', 'not_fengban', 'fengban_rate'])
    date_list = []
    for key in zhangting_rate_dict:
        print (key)
        fengban_list = fengban_dict[key]
        notfeng_list = notfeng_dict[key]
        date_list.append(key)
        df.set_value('r', 't', 'a', 'e')
        # df.set_value(key, len(fengban_list), len(notfeng_list), zhangting_rate_dict[key])
        print ([key, len(fengban_list), len(notfeng_list), zhangting_rate_dict[key]])
    print (df)




# def sort():
#     global zhangting_rate_dict
#     zhangting_rate_dict = read_zhangting_rate_dict()
#     fengban_dict = zhangting.get_fengban_dict()
#     notfeng_dict = zhangting.get_notfeng_dict()
#     datetime_list = []
#     date_list = []
#     rate_list = []
#     fengban_list = []
#     notfeng_list = []
#     for key in zhangting_rate_dict:
#         date_list.append(key)
#     date_list.sort()
#     for datestring in date_list:
#         rate_list.append(zhangting_rate_dict[datestring])
#         list = fengban_dict[datestring]
#         fengban_list.append(len(list))
#         list = notfeng_dict[datestring]
#         notfeng_list.append(len(list))
#         datekey = datetime.datetime.strptime(datestring, '%Y-%m-%d')
#         datetime_list.append(datekey)
#     print (date_list)
#     print (rate_list)
#     print (fengban_list)
#     print (notfeng_list)
#     print (datetime_list)
#     plt.plot_date(matplotlib.dates.date2num(datetime_list), rate_list, linestyle='-')
#     plt.show()


def zhangting_rate_chart():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')  # 为y轴加注释
    plt.show()



if __name__ == '__main__':
    # caculate_fengban_rate()
    # save_zhangting_rate()
    # zhangting_rate_chart()
    fengban_df()