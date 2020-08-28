# encoding: utf-8
# !/usr/bin/python3

from pi_server.cache import PiServerCache
from pi_server.cache.cache_entity.Tcp import TcpChannelCacheEntity
from pi_common.communication.tcp.tcp_Interface.TcpChannelHandle import TcpChannelHandle
import time
"""
服务器端TCP服务端连接处理器

"""


class ClientTcpClientChannelHandle(TcpChannelHandle):

    @staticmethod
    def addTcpChannel(address, channel):
        PiServerCache.tcpServiceChannelMapCache.put(str(address), TcpChannelCacheEntity(address, channel))  # 通道存储到缓存

    @staticmethod
    def removeTcpChannel(address):
        PiServerCache.tcpServiceChannelMapCache.removeChannel(address)

    @staticmethod
    def updateTcpChannelDate(address, data):
        tcpchabbe = PiServerCache.tcpServiceChannelMapCache.get(address)
        time_ = time.time()
        tcpchabbe.heartbeatTime = time_
        tcpchabbe.transmissionTime = time_
        tcpchabbe.transmissionLen += len(data)
