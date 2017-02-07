# -*- coding: utf-8 -*-

import fengban_rate
import paotaidixi
import rate_of_fengban
import stock
import zhangting

if __name__ == '__main__':
    stock.downloadToday()
    stock.downloadHistory()
    zhangting.zhangting()
    fengban_rate.caculate_fengban_rate()
    rate_of_fengban.caculate_rou()
    paotaidixi.dapao()