# encoding: UTF-8

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine
from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
from vnpy.api.huobi.HuobiTrader import HoubiTrader
import math


class runOnlinBackTesting():
    def __init__(self):
        self.base = "eos"
        self.quote = "btc"
        self.symbol = self.base + self.quote
        self.huobiApi = HoubiTrader().getApi()
        self.engine = BacktestingEngine()
        self.doInit()

    def doInit(self):
        # 获取交易对的价格精度和最小交易数量
        pricePrecision, amountPrecision = self.huobiApi.get_symbol_precision(self.base, self.quote)
        self.priceTicker = 1.0 / pow(10, pricePrecision)
        self.amountTicker = 1.0 / pow(10, amountPrecision)

        self.engine.setBacktestingMode(self.engine.BAR_MODE)
        self.engine.setSlippage(self.priceTicker * 2)  # 滑点
        self.engine.setRate(0.2 / 100)  # 手续费
        self.engine.setSize(1)
        self.engine.setPriceTick(self.priceTicker)  # 最小价格变动
        self.engine.tradeAPI = self.huobiApi
        self.engine.symbol = self.symbol

        # 在引擎中创建策略对象
        d = {}
        self.engine.initStrategy(KkStrategy, d)

    def start(self, theradName = "1" , count = "2"):
        print(theradName + "---" + count)
        # 开始跑回测
        self.engine.runOnlinBacktesting()

    def getLogger(self):
        logQueue = self.engine.logQueue
        return logQueue

if __name__ == '__main__':
    backTest = runOnlinBackTesting()
    backTest.doInit()
    backTest.start()

'''
if __name__ == '__main__':
    base = 'eos'
    quote = 'btc'
    symbol = base+quote
    huobiApi = HoubiTrader().getApi()

    # 获取交易对的价格精度和最小交易数量
    pricePrecision, amountPrecision = huobiApi.get_symbol_precision(base,quote)
    priceTicker = 1.0 / pow(10, pricePrecision)
    amountTicker = 1.0 / pow(10, amountPrecision)

    engine = BacktestingEngine()
    engine.setBacktestingMode(engine.BAR_MODE)
    engine.setSlippage(priceTicker * 2)  # 滑点
    engine.setRate(0.2 / 100)  # 手续费
    engine.setSize(1)
    engine.setPriceTick(priceTicker)  # 最小价格变动
    engine.tradeAPI = huobiApi
    engine.symbol = symbol





    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(KkStrategy, d)

    # 开始跑回测
    engine.runOnlinBacktesting()

    # engine.showBacktestingResult()

    # print("priceTicker:",1.0 / pow(10,pricePrecision))
    # print("amountTicker:", 1.0 / pow(10, amountPrecision))

    # print(price, " ", amount)



    # engine = BacktestingEngine()
    #
    # engine.setBacktestingMode(engine.BAR_MODE)
    #
    # engine.setStartDate("20180901")
    # symbol = "eosbtc"
    #
    # engine.setSlippage(0.00000002)  # 滑点
    # engine.setRate(0.2/100)  # 手续费
    # engine.setSize(1)  # 股指合约大小
    # engine.setPriceTick(0.00000001)  # 股指最小价格变动
    # engine.setCapital(0.02)
    #
    # # 设置使用的历史数据库
    # engine.setDatabase('huobi', 'eosbtc_60min')
    #
    # # 在引擎中创建策略对象
    # d = {}
    # engine.initStrategy(KkStrategy, d)
    #
    # # 开始跑回测
    # engine.runBacktesting()
    #
    # # 显示回测结果
    # engine.showBacktestingResult()
'''