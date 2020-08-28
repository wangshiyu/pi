# encoding: utf-8
# !/usr/bin/python3


"""核心类"""

from pi_common.log.LoggingFactory import logger
from pi_common.communication.tcp.server.TcpSocketServer import TcpSocketServer
from pi_server.core.execute_processor.ServerExecuteSelector import ServerExecuteSelector
from pi_server.core.execute_processor.ServerTcpServiceChannelHandle import ServerTcpServiceChannelHandle
import threading
import sys,os
from pi_common.config.Config import Config,ConfigEnum
import time


class ServerCore:
    __tcpSocketServer = None

    def __init__(self):
        pass

    def init(self):
        host = 'localhost'
        port = 6162
        address = Config.getConfig(ConfigEnum.ADDRESS)
        if address is not None:
            host = address.split(':')[0]
            port = address.split(':')[1]
        logger.info("ServerCode Start ...")
        self.__tcpSocketServer = TcpSocketServer(host,int(port))
        self.__tcpSocketServer.tcpServiceChannelHandle = ServerTcpServiceChannelHandle()
        self.__tcpSocketServer.executeSelector = ServerExecuteSelector()
        # _thread.start_new_thread(self.__tcpSocketServerInit, ())
        t = threading.Thread(target=self.__tcpSocketServerInit, args=())
        logger.info("ServerCode Start tcpSocketServer Success! port:" + str(self.__tcpSocketServer.port))
        logger.info("ServerCode Start Success!")
        t.start()
        t.join()

    def __tcpSocketServerInit(self):
        self.__tcpSocketServer.createTcpSocketServer()