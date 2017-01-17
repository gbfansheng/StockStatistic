# -*- coding: utf-8 -*-
import pandas as pd
import tushare as ts
import os
import datetime

def downloadToday():
	df = ts.get_today_all()
	df.to_csv('today.csv',sep=',', encoding='utf-8')
	pass

def get_today():
	todayDf = pd.read_csv('today.csv',sep=',', encoding='utf-8', dtype = str)
	return todayDf

def read(code):
	fileName = code + '.csv'
	df = pd.read_csv(fileName, sep=',', encoding='utf-8', dtype = str)
	return df

def downloadHistory():
	todayDF = get_today()
	codeList = list(todayDF['code'])
	print(codeList)
	for code in codeList:
		fileName = code + '.csv'
		print('fileName:' + fileName)
		#文件是否存在
		if os.path.isfile(fileName):
			##处理时间
			codeDF = read(code)
			dateList = list(codeDF['date'])
			dateString = dateList[0:1][0]
			print('date:' + dateString)
			nowdt = datetime.datetime.now()
			nowdtstring = nowdt.strftime('%Y-%m-%d')
			print('nowdtstring:' + nowdtstring)
			if dateString == nowdtstring:
				pass
			else :
				##获取两日日期之间的数据	
				dt = datetime.datetime.strptime(dateString, '%Y-%m-%d')
				dt = dt + datetime.timedelta(days = 1)
				dtstring = dt.strftime('%Y-%m-%d') 
				additionDF = ts.get_hist_data(code = code, start = dtstring, end = nowdtstring)
				concatDF = additionDF.append(codeDF)
				concatDF.to_csv(code + '.csv')
		else:
			df = ts.get_hist_data(code)
			df.to_csv(code + '.csv')


if __name__=='__main__':   
	downloadToday()
	downloadHistory()