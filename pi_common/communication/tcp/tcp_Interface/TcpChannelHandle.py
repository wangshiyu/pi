# encoding: utf-8
# !/usr/bin/python3
import abc

"""
TCP连接通道处理器

"""


class TcpChannelHandle(metaclass=abc.ABCMeta):  # 抽象类
    @abc.abstractmethod  ## tcp添加连接
    def addTcpChannel(address, channel):
        pass

    @abc.abstractmethod  ## 删除tcp连接
    def removeTcpChannel(address):
        pass

    @abc.abstractmethod  ## tcp数据更新
    def updateTcpChannelDate(address, data):
        pass
