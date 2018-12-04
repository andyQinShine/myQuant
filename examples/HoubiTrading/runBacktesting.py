# encoding: UTF-8

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine
from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
if __name__ == '__main__':
    engine = BacktestingEngine()

    engine.setBacktestingMode(engine.BAR_MODE)

    engine.setStartDate("20180901")
    symbol = "eosbtc"

    engine.setSlippage(0.00000002)  # 滑点
    engine.setRate(0.2/100)  # 手续费
    engine.setSize(1)  # 股指合约大小
    engine.setPriceTick(0.00000001)  # 股指最小价格变动
    engine.setCapital(0.02)

    # 设置使用的历史数据库
    engine.setDatabase('huobi', 'eosbtc_60min')

    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(KkStrategy, d)

    # 开始跑回测
    engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()