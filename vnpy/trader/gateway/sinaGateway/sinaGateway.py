# encoding: UTF-8

from vnpy.trader.vtGateway import *
from vnpy.api.sina.vnsina import DataApi


class SinaGateway(VtGateway):
    def __init__(self):
        self.DataApi = DataApi()

    def connection(self):
        self.DataApi.active = True