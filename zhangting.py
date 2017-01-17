# -*- coding: utf-8 -*-
import pandas as pd
import stock
import datetime

def processDf(code, df):
	global dateDict
	# begin = datetime.date(2014,1,19)  
    end = datetime.datetime.now()
    for i in range((end - begin).days+1):  
        day = begin + datetime.timedelta(days=i)  
        print str(day) 
		daystring = day.strftime('%Y-%m-%d')
		dfForDay = df[df['date'].isin([daystring])]
		datelist = dateDict[daystring]
		
		if datelist:
			pass
		else :
			datelist = []

		#当天有数据
		if dfForDay:
			p_change = dfForDay['p_change'][0]
			high = dfForDay['high'][0]
			close = dfForDay[close][0]
			if float(p_change) > 9.9 and float(high) == float(close):
				#如果涨停则保存
				print('append')
				datelist.append(code)
				dateDict[daystring] = datelist


def zhangting():
	global dateDict
	# todayDF = stock.get_today()
	# codeList = list(todayDF['code'])
	# for code in codeList:
		code = '300505'
		codeDF = stock.read(code)
		#文件是否存在
		if codeDF:
			processDf(code, codeDF)
	print(dateDict)

if __name__=='__main__':   
	zhangting()