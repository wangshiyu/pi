# encoding: utf-8
# !/usr/bin/python3

import socket
import _thread
from pi_common.log.LoggingFactory import logger
from pi_common.util.Base64Util import b64decode
from pi_common.util.SerializeUtil import bytsToObj
from pi_common.constant.DictKeyConstant import DictKeyConstant

'''
server端
长连接，短连接，心跳
'''


class TcpSocketServer:
    bufSize = 1024  # 缓存区大小
    host = 'localhost'  # ip
    port = 6162  # 端口
    listen = 10  # 最大连接数
    executeSelector = None  # 指令选择器
    tcpServiceChannelHandle = None  # TCP 通道处理器

    def __init__(self, host='localhost', port=6162, bufSize=1024, listen=10):
        self.host = host
        self.port = port
        self.bufSize = bufSize
        self.listen = listen

    def createTcpSocketServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(self.listen)  # 接收的连接数
        while True:
            channel, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收

            if self.tcpServiceChannelHandle is not None: self.tcpServiceChannelHandle.addTcpChannel(address, channel)
            # Cache.tcpServiceChannelMapCache.put(str(address), TcpChannelCacheEntity(address, channel))  # 通道存储到缓存
            try:
                _thread.start_new_thread(self.__client, (channel, address))
                logger.info("建立线程:" + str(address))
            except:
                logger.error("Error: 无法启动线程")

    # 为线程定义一个函数
    def __client(self, channel, address):
        address_str = str(address)
        while True:  # 循环收发数据包，长连接
            command_id = None
            byteData = None
            try:
                base64Date = channel.recv(self.bufSize)
                if base64Date is None or len(base64Date) == 0:
                    logger.info("base64Date is None!!!")
                    if self.tcpServiceChannelHandle is not None: self.tcpServiceChannelHandle.removeTcpChannel(
                        address_str)  # 清理缓存数据
                    logger.info("connect close:" + address_str)
                    channel.close()  # 断开连接
                    break
                byteData = b64decode(base64Date)
                msg = bytsToObj(byteData)
                command_id = msg.id
                dict = {}
                dict[DictKeyConstant.COMMANDS] = msg.data
                dict[DictKeyConstant.ADDRESS] = address_str
                if self.executeSelector is not None: self.executeSelector.addMsg(dict)  # 添加到指令处理器
            except Exception as e:
                # TcpSocketServiceMsgSend.sendMsgStr(channel,"data is error!!!",command_id,ResultTypeEnum.pi_log._value_)
                #if self.tcpServiceChannelHandle != None : self.tcpServiceChannelHandle.removeTcpChannel(address_str)
                logger.info("data is error!!!")
                logger.error(str(e))
                logger.info(address_str + "connect close!")
                #channel.close()  # 断开连接
                # break

            if self.tcpServiceChannelHandle is not None: self.tcpServiceChannelHandle.updateTcpChannelDate(address_str,
                                                                                                           byteData)


if __name__ == "__main__":
    tss = TcpSocketServer()
    tss.createTcpSocketServer()
