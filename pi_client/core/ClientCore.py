# encoding: utf-8
# !/usr/bin/python3


from pi_common.communication.tcp.client.TcpSocketClient import TcpSocketClient
from pi_common.log.LoggingFactory import logger
from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_client.cache.cache_entity.Tcp import TcpChannelCacheEntity
from pi_client.core.execute_processor.ClientExecuteSelector import ClientExecuteSelector
from pi_client.core.execute_processor.ClientTcpServiceChannelHandle import ClientTcpClientChannelHandle

"""客户端核心类"""


class ClientCore:
    def __init__(self):
        pass

    # 服务初始化类
    def init(self):
        logger.info("ClientCore Start ...")

        # logger.info("ClientCore Start tcpSocketServer Success! port:" + str(self.__tcpSocketServer.port))
        logger.info("ClientCore Start Success!")

    # 创建客户端
    def createClient(self, host, port):
        address = host + ":" + str(port)
        tcpChannelCacheEntity = tcpServiceChannelMapCache.get(address)
        if (tcpChannelCacheEntity is None):
            tcpSocketClient = TcpSocketClient(host, port)
            tcpSocketClient.executeSelector = ClientExecuteSelector()
            tcpSocketClient.tcpServiceChannelHandle = ClientTcpClientChannelHandle()
            tcpSocketClient.createTcpSocketClient()
            tcpChannelCacheEntity = TcpChannelCacheEntity(address, tcpSocketClient)
            tcpServiceChannelMapCache.put(address, tcpChannelCacheEntity)
