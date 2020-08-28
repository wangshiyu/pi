# encoding: utf-8
# !/usr/bin/python3

"""
客户端数据发送封装类
"""
from pi_common.communication.msg.TcpMsg import TcpMsg
import uuid
from pi_common.util.Base64Util import b64encode
from pi_common.util.SerializeUtil import objToByts
from pi_common.command_set.Command import Command
import time


class TcpSocketClientMagSend:

    @staticmethod
    def sendMsgStr(channel, str, command_id=None, resultType=None):
        pass

    @staticmethod
    def sendMsgCommand(channel, commands):
        msg = TcpMsg()
        msg.data = commands
        TcpSocketClientMagSend.sendMsg(channel, msg)

    @staticmethod
    def sendMsg(channel, msg):
        msg.id = uuid.uuid1()
        msg.timeStamp = time.time()
        byte_ = objToByts(msg)
        byte_data = b64encode(byte_)
        channel.send(byte_data)  # 返回信息
