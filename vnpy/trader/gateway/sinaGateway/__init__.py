# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .sinaGateway import SinaGateway

gatewayClass = SinaGateway
gatewayName = 'SINA'
gatewayDisplayName = u'新浪'
gatewayType = vtConstant.GATEWAYTYPE_BTC
gatewayQryEnabled = False