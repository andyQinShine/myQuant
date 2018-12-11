# encoding: UTF-8

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine
from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
from vnpy.api.huobi.HuobiTrader import HoubiTrader
import math
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