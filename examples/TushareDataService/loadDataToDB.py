# encoding: UTF-8

import tushare as ts
import json
import pymongo
from pymongo import MongoClient, ASCENDING
from vnpy.trader.vtObject import VtBarData
from datetime import datetime, timedelta
import time

# 加载配置
config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']


mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
# db = mc[MINUTE_DB_NAME]                         # 数据库

class loadTushareData():
    def __init__(self, symbol, fre='60min'):
        self.symbol = symbol
        self.fre = fre
        self.collection = mc[setting['CLIENT']][symbol + "_" + fre]
        self.collection.ensure_index([('datetime', pymongo.ASCENDING)], unique=True)
        self.fromDate = '20180801'
        self.endDate = None

        # init tu share info
        ts.set_token(setting['TUSHARE_TOKEN'])
        self.tsApi = ts.pro_api()

    def loadData(self, fromDate, endDate):
        df = self.tsApi.query('coinbar', exchange=setting['CLIENT'], symbol = self.symbol, freq=self.fre, start_date=fromDate,
                       end_date=endDate)
        print(df)
        for index,rows in df.iterrows():
            bar = VtBarData()
            bar.vtSymbol = rows["symbol"]
            bar.symbol = rows["symbol"]
            bar.open = float(rows['open'])
            bar.high = float(rows['high'])
            bar.low = float(rows['low'])
            bar.close = float(rows['close'])
            date = datetime.strptime(rows['date'], "%Y-%m-%d %H:%M:%S")
            bar.date = date.strftime('%Y%m%d')
            bar.time = date.strftime('%H:%M:%S')
            bar.datetime = datetime.strptime(bar.date + ' ' + bar.time, '%Y%m%d %H:%M:%S')
            bar.volume = rows['vol']

            flt = {'datetime': bar.datetime}
            self.collection.update_one(flt, {'$set': bar.__dict__}, upsert=True)




client = loadTushareData('eosbtc',fre='15min')
startDate = '20180801'
timeNow = datetime.now().strftime('%Y%m%d')
endTime = datetime.strptime(timeNow,'%Y%m%d') - timedelta(1)
startTime = datetime.strptime(startDate,'%Y%m%d')

print(startTime <= endTime)
while startTime <= endTime:
    fromDate = startTime.strftime('%Y%m%d')
    endDate = (startTime + timedelta(1)).strftime('%Y%m%d')
    client.loadData(fromDate,endDate)
    time.sleep(1)
    startTime = startTime + timedelta(1)
# while True:
#
#
# self.startDate = startDate
# self.initDays = initDays
#
# dataStartDate = datetime.strptime(startDate, '%Y%m%d')
#
# initTimeDelta = timedelta(1)
# self.strategyStartDate = self.dataStartDate + initTimeDelta
#
# client.loadData('20181101', '20181116')
