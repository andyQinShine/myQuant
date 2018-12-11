# encoding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from vnpy.api.huobi.vnhuobi import TradeApi

#----------------------------------------------------------------------
def testTrade():
    """测试交易"""
    accessKey = 'abf6aa47-0fc6e16d-54568d9a-5eb6f'
    secretKey = 'eb0af62e-aa4cb74a-e8e5289c-c9fe3'
    
    # 创建API对象并初始化
    api = TradeApi()
    
    api.init(api.HUOBI, accessKey, secretKey, mode=api.SYNC_MODE)
    api.start()
    
    # 查询
    print(api.getSymbols())
    # print(api.getCurrencys())
    # print(api.getTimestamp())


    
    
    #accountid = ''
    symbol = 'eosbtc'
    
    #api.getAccounts()
    #api.getAccountBalance(accountid)
    #api.getOrders(symbol, 'pre-submitted,submitted,partial-filled,partial-canceled,filled,canceled')
    #api.getOrders(symbol, 'filled')
    # print(api.getMatchResults(symbol))

    dataKline = api.getKline(symbol, '5min')
    print("===============",dataKline)

    dataMerged = api.getMerged(symbol)
    print("===============", dataMerged)
    
    #api.getOrder('2440401255')
    #api.getMatchResult('2440401255')
    
    #api.placeOrder(accountid, '2', symbol, 'sell-market', source='api')
    #api.cancelOrder('2440451757')
    #api.batchCancel(['2440538580', '2440537853', '2440536765'])
    
    input()    


    
    
if __name__ == '__main__':
    testTrade()