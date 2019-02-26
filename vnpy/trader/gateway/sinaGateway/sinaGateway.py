# encoding: UTF-8

from vnpy.trader.vtGateway import *
from vnpy.api.sina.vnsina import DataApi
from vnpy.trader.vtFunction import getJsonPath
import json
import time

class SinaGateway(VtGateway):
    def __init__(self, eventEnginer, gatewayName='SINA'):
        super(SinaGateway, self).__init__(eventEngine, gatewayName)
        self.dataApi = SinaDataApi()
        self.gatewayName = gatewayName

        self.fileName = self.gatewayName + '_connect.json'
        self.filePath = getJsonPath(self.fileName, __file__)


    def connection(self):
        try:
            f = open(self.filePath)
        except IOError:
            log = VtLogData()
            log.gatewayName = self.gatewayName
            log.logContent = u'读取连接配置出错，请检查'
            self.onLog(log)
            return

        # 解析json文件
        setting = json.load(f)
        try:
            exchange = str(setting['exchange'])
            symbols = setting['symbols']
        except KeyError:
            log = VtLogData()
            log.gatewayName = self.gatewayName
            log.logContent = u'连接配置缺少字段，请检查'
            self.onLog(log)
            return

        # 订阅对应的股票信息
        self.dataApi.subStocks(symbols)


class SinaDataApi(DataApi):
    def __init__(self):
        super(SinaDataApi,self).__init__(True)

    def onTickData(self):
        print "override on tick data"
        for symbol in self.subSymbols:
            data = self.subSymbols[symbol]
            tick = VtTickData()
            tick.symbol = symbol
            # 今日开盘价
            tick.openPrice = float(data[0])
            # 昨日收盘价
            tick.yClose = float(data[1])
            # 当前价格
            tick.lastPrice = float(data[2])
            # 今日最高价
            tick.highPrice = float(data[3])
            # 今日最低价
            tick.lowPrice = float(data[4])
            # 竞买价，即“买一”报价
            tick.bidPrice1 = float(data[5])
            # 竞卖价，即“卖一”报价；
            tick.askPrice1 = float(data[6])
            # 成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百
            tick.volume = int(data[7])
            # 成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万
            tick.volumeCash = float(data[8])
            # “买一”申请4695股，即47手；
            tick.bidVolume1 = int(data[9])
            # “买一”报价；
            tick.bidPrice1 = float(data[10])

            tick.bidVolume2 = int(data[11])
            tick.bidPrice2 = float(data[12])

            tick.bidVolume3 = int(data[13])
            tick.bidPrice3 = float(data[14])

            tick.bidVolume4 = int(data[15])
            tick.bidPrice4 = float(data[16])

            tick.bidVolume5 = int(data[17])
            tick.bidPrice5 = float(data[18])

            tick.askVolume1 = int(data[19])
            tick.askPrice1 = float(data[20])

            tick.askVolume2 = int(data[21])
            tick.askPrice2 = float(data[22])

            tick.askVolume3 = int(data[23])
            tick.askPrice3 = float(data[24])

            tick.askVolume4 = int(data[25])
            tick.askPrice4 = float(data[26])

            tick.askVolume5 = int(data[27])
            tick.askPrice5 = float(data[28])


            tick.date = data[29]
            tick.time = data[30]


            print (tick.__dict__)


if __name__ == '__main__':
    gateWay = SinaGateway(None)
    gateWay.connection()
    while True:
        time.sleep(60)