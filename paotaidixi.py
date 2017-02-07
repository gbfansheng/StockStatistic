# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import datetime
import stock
import zhangting
import copy
import xlwt


def dapao():
    fengban_dict = zhangting.get_fengban_dict()
    now = datetime.datetime.now().date()
    df_list = []
    fengban_list = []
    fengban_acc_list = []
    total_code_list = []
    total_delta_list = []
    range_day = 21
    for i in range(range_day):
        zhangting_day = now - datetime.timedelta(days=(range_day - i))
        zhangting_daystring = zhangting_day.strftime('%Y-%m-%d')
        ban_list = fengban_dict.get(zhangting_daystring, [])
        if len(ban_list) > 0:
            print zhangting_daystring
            fengban_acc_list.append(copy.deepcopy(ban_list))

    for i in range(len(fengban_acc_list)):
        ban_list = fengban_acc_list[i]
        code_list = []
        delta_list = []
        for code in ban_list:
            df = stock.read(code)
            df = df[0:(len(fengban_acc_list) - i)]
            high_list = list(df['high'])
            highest = float(max(high_list))
            close = list(df['close'])
            current = float(close[0])
            delta = current / highest - 1
            code_list.append(code)
            delta_list.append(delta)
            if not total_code_list.__contains__(code):
                total_code_list.append(code)
                total_delta_list.append(delta)
        delta_list_name = str((len(fengban_acc_list) - i)) + 'delta'
        code_list_name = str((len(fengban_acc_list) - i)) + 'code'
        df = pd.DataFrame({code_list_name: code_list, delta_list_name: delta_list})
        df = df.sort_values(by=delta_list_name)
        df_list.append(df)
    df = pd.DataFrame({'0code': total_code_list, '0delta': total_delta_list})
    df = df.sort_values(by = '0delta')
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
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet("炮架", cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'  # 指定“宋体”
    style.font = font
    name_dict = stock.get_name_dict()
    for i in range(len(df_list)):
        df = df_list[i]
        code_colums_name = str(len(df_list) - i - 1) + 'code'
        delta_colums_name = str(len(df_list) - i - 1) + 'delta'
        code_list = list(df[code_colums_name])
        delta_list = list(df[delta_colums_name])
        sheet.write(0, i * 3, '代码')
        sheet.write(0, i * 3 + 1, '代码名称')
        sheet.write(0, i * 3 + 2, str(len(df_list) - i - 1) + '日涨停跌幅排行')
        for j in range(len(code_list)):
            sheet.write(j + 1, i * 3, code_list[j])
            sheet.write(j + 1, i * 3 + 1, name_dict.get(code_list[j], ' '))
            sheet.write(j + 1, i * 3 + 2, delta_list[j])

    workbook.save(stock.get_data_path() + '低吸打炮.xls')


if __name__ == '__main__':
    dapao()