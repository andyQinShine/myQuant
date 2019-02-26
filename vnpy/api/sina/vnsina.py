# encoding: utf-8

from threading import Thread
import time
import urllib
import requests

class DataApi(object):

    def __init__(self, active = False):
        self.url = 'http://hq.sinajs.cn/list'

        self.reqid = 0
        self.active = active
        self.subThread = Thread(target=self.run)
        self.subSymbols = {}

    def httpGet(self, url, params=None):
        """HTTP GET"""
        headers = {'content-type': 'charset=utf-8'}
        postdata = None
        if params:
            postdata = urllib.urlencode(params)

        try:
            response = requests.get(url, postdata,headers=None, timeout=5)
            if response.status_code == 200:
                content = response.content
                content = content.decode('gb2312','ignore').encode('utf-8')
                return True,content
            else:
                return False, u'GET请求失败，状态代码：%s' % response.status_code
        except Exception as e:
            return False, u'GET请求触发异常，原因：%s' % e

    def run(self):
        while self.active:
            requesturl =self.url + "=" + ",".join(self.subSymbols.keys())
            result,data = self.httpGet(requesturl)
            if result is True:
                self.handelSubData(data)
                self.onTickData()
            time.sleep(1)

    def handelSubData(self, data):
        tick_list = data.split(';')
        for tick in tick_list:
            tick_data = tick.split(',')
            for symbol in self.subSymbols.keys():
                if symbol in tick_data[0]:
                    self.subSymbols[symbol] = tick_data[1:]

    def subStocks(self, symbols):
        for symbol in symbols:
            symbol = str(symbol)
            if self.subSymbols.has_key(symbol) == False:
                self.subSymbols[symbol] = None
        self.subThread.run()

    def onTickData(self):
        print self.subSymbols


if __name__ == '__main__':
    dataApi = DataApi()
    dataApi.active = True
    dataApi.subStocks(['sz002326'])