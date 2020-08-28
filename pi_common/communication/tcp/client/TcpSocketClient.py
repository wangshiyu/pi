# encoding: utf-8
# !/usr/bin/python3

import _thread
import socket
from pi_common.log.LoggingFactory import logger
from pi_common.util.Base64Util import b64decode
from pi_common.util.SerializeUtil import bytsToObj

"""
TCP通讯客户端
"""


class TcpSocketClient:
    bufSize = 1024  # 缓存区大小
    host = None  # 地址
    port = None  # 端口
    channel = None  # 客户端通道
    closeFalg = False  # 关闭
    executeSelector = None  # 指令选择器
    tcpServiceChannelHandle = None  # TCP 通道处理器

    def __init__(self, host, port):
        self.host = host
        self.port = port
        pass

    def createTcpSocketClient(self):
        self.channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.channel.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 在客户端开启心跳维护
        self.channel.connect((self.host, self.port))
        address = self.host + ":" + str(self.port)
        try:
            _thread.start_new_thread(self.__client, (self.channel, address))
            logger.info("建立线程:" + address)
        except:
            logger.error("Error: 无法启动线程")

    def sendMag(self, msg):
        self.channel.send(msg)

    def close(self):
        self.closeFalg = True
        self.channel.close()

    # 为线程定义一个函数
    def __client(self, channel, address):
        address_str = str(address)
        while self.closeFalg != False:  # 循环收发数据包，长连接
            command_id = None
            byteData = None
            try:
                base64Date = channel.recv(self.bufSize)
                if base64Date is None or len(base64Date) == 0:
                    channel.close()  # 断开连接
                    #  Cache.tcpServiceChannelMapCache.removeChannel(address_str)  # 清理缓存数据
                    logger.info("connect close:" + address_str)
                    break
                byteData = b64decode(base64Date)
                msg = bytsToObj(byteData)
                if self.executeSelector !=None :self.executeSelector.addMsg(msg,address_str)
            except Exception:
                channel.close()  # 断开连接
                logger.info("data is error!!!")
                logger.info(address_str + "connect close!")
                break

# if __name__ == "__main__":
#     tsc = TcpSocketClient("localhost", 6162)
#     tsc.createTcpSocketClient()
#     msg = TcpMsg()
#     msg.id = uuid.uuid1()
#     msg.timeStamp = time.time()
#     list = list()
#     command= DirectiveCommand()
#     command.queueName="duoji01"
#     command.id=uuid.uuid1()
#     command.commandType=CommandTypeEnum.pi_directive._value_
#     list.append(command)
#     msg.data = list
#     byte_ = objToByts(msg)
#     byte_data = b64encode(byte_)
#     tsc.sendMag(byte_data)
#     while True:
#         pass
