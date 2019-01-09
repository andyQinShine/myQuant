# -*- coding: utf-8 -*-
# author: 半熟的韭菜

import websocket
from websocket import create_connection
import gzip
import time

if __name__ == '__main__':
    while (1):
        try:
            ws = create_connection("wss://api.huobi.pro/ws",http_proxy_host = "127.0.0.1",http_proxy_port =1080 )
            # ws = websocket.WebSocket()
            # ws.connect("wss://api.huobi.pro/ws", http_proxy_host="127.0.0.1", http_proxy_port=1080)
        except Exception, e:
            print(str(Exception))
            print(str(e))
            print('connect ws error,retry...')
            time.sleep(5)

    # 订阅 KLine 数据
    tradeStr="""{"sub": "market.htusdt.kline.1min","id": "id10"}"""

    # 请求 KLine 数据
    # tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""

    # 订阅 Market Depth 数据
    # tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 请求 Market Depth 数据
    # tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 订阅 Trade Detail 数据
    tradeStr = {"sub": "market.btcusdt.trade.detail", "id": "id10"}

    # 请求 Trade Detail 数据
    # tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

    # 请求 Market Detail 数据
    # tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""

    ws.send(tradeStr)
    trade_id = ''
    while (1):
        compressData = ws.recv()
        result = gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts = result[8:21]
            pong = '{"pong":' + ts + '}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            try:
                if trade_id == result['data']['id']:
                    print('重复的id')
                    break
                else:
                    trade_id = result['data']['id']
            except Exception:
                pass

            print(result)


