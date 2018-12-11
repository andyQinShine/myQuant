import json
import os
from vnhuobi import TradeApi
from vnpy.trader.vtFunction import getJsonPath

class HoubiTrader(object):
    current_path = os.path.abspath(__file__)
    path = getJsonPath('config.json', __file__)
    config = open("./config.json")
    setting = json.load(config)

    accessKey = setting['accessKey']
    secretKey = setting['secretKey']
    inited = False

    def __init__(self):
        self.api = TradeApi()
        if not self.inited:
            self.api.init(self.api.HUOBI, self.accessKey, self.secretKey, mode=self.api.SYNC_MODE)
        self.api.start()

    def getApi(self):
        return self.api


if __name__ == '__main__':
    api = HoubiTrader().getApi()
    price, amount = api.get_symbol_precision('eos', 'btc')
    print("price precision is %d, amount precision is %d",price ,amount)