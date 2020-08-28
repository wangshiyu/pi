# encoding: utf-8
# !/usr/bin/python3
import time
from pi_common.log.LoggingFactory import logger
"""
TCP 通道缓存实体
"""


class TcpChannelCacheEntity:
    address = None  # 地址
    createTime = time.time()  # 建立时间
    heartbeatTime = time.time()  # 上次心跳时间
    transmissionLen = 0  # 传输字节长度
    transmissionTime = None  # 上次传输时间
    auth = None
    tcpSocketClient = None

    def __init__(self, address, tcpSocketClient):
        self.address = address
        self.tcpSocketClient = tcpSocketClient

    """
    断开连接
    """

    def channelClose(self):
        self.tcpSocketClient.close =True
        self.tcpSocketClient.channel.close()
        logger.info("连接主动断开:" + str(self.address))

#
# def setHeartbeatTime(self,heartbeatTime):
#     self.heartbeatTime=heartbeatTime
#
# def setTransmissionLen(self,transmissionLen):
#     self.transmissionLen=transmissionLen
#
# def setTransmissionTime(self,transmissionTime):
#     self.transmissionTime=transmissionTime
