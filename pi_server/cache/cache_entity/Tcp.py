# encoding: utf-8
# !/usr/bin/python3
import time
from pi_common.log.LoggingFactory import logger
"""
TCP 通道缓存实体
"""


class TcpChannelCacheEntity:
    address = None  # 地址
    channel = None  # 连接通道
    createTime = time.time()  # 建立时间
    heartbeatTime = time.time()  # 上次心跳时间
    transmissionLen = 0  # 传输字节长度
    transmissionTime = None  # 上次传输时间
    auth = None

    def __init__(self, address, channel):
        self.address = address
        self.channel = channel

    """
    断开连接
    """

    def channelClose(self):
        self.channel.close()
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
