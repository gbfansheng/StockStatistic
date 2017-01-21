# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import datetime
import stock
import zhangting
import copy


def dapao():
    fengban_dict = zhangting.get_fengban_dict()
    now = datetime.datetime.now().date()
    df_list = []
    fengban_list = []
    fengban_acc_list = []
    print fengban_dict
    range_day = 10
    for i in range(range_day):
        zhangting_day = now - datetime.timedelta(days=(range_day - i))
        zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
        ban_list = fengban_dict.get(zhangting_daystring, [])
        if len(ban_list) > 0:
            print zhangting_daystring
            fengban_list.extend(ban_list)
            fengban_acc_list.append(copy.deepcopy(fengban_list))

    for i in range(len(fengban_acc_list)):
        ban_list = fengban_acc_list[i]
        code_list = []
        delta_list = []
        for code in ban_list:
            df = stock.read(code)
            df = df[0:(len(fengban_acc_list) - i)]
            high_list = list(df['high'])
            highest = float(max(high_list))
            print highest
            close = list(df['close'])
            current = float(close[0])
            print current
            delta = current / highest - 1
            code_list.append(code)
            delta_list.append(delta)
        delta_list_name = str((len(fengban_acc_list) - i)) + '日跌幅'
        code_list_name = str((len(fengban_acc_list) - i)) + '日代码'
        df = pd.DataFrame({code_list_name: code_list, delta_list_name: delta_list})
        df = df.sort_values(by=delta_list_name)
        df_list.append(df)
    save_df(df_list)


    # for i in range(10):
    #     zhangting_day = now - datetime.timedelta(days=(10 - i))
    #     zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
    #     fengban_list.extend(fengban_dict.get(zhangting_daystring, []))
    #     print 'i=',i,'   ',fengban_list
    #     code_list = []
    #     delta_list = []
    #     if len(fengban_list) > 0:
    #         for code in fengban_list:
    #             print code
    #             df = stock.read(code)
    #             df = df[0:(10 - i)]
    #             high_list = list(df['high'])
    #             highest = float(max(high_list))
    #             print highest
    #             close = list(df['close'])
    #             current = float(close[0])
    #             print current
    #             delta = current / highest - 1
    #             code_list.append(code)
    #             delta_list.append(delta)
    #         df = pd.DataFrame({'code':code_list, 'delta':delta_list})
    #         df = df.sort_values(by = 'delta')
    #         df_list.append(df)
    #     save_df(df_list)

def save_df(df_list):
    for i in range(len(df_list)):
        name = str(len(df_list) - i) + '日跌幅'
        stock.save(df_list[i], name=name)

if __name__ == '__main__':
    dapao()