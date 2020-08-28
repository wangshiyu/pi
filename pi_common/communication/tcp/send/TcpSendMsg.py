# encoding: utf-8
# !/usr/bin/python3
from pi_common.communication.msg.Msg import Msg
from pi_common.communication.msg.TcpMsg import TcpMsg
import uuid
from pi_common.util.Base64Util import b64encode
from pi_common.util.SerializeUtil import objToByts
from pi_common.constant.enums.MsgTypeEnum import MsgTypeEnum
import time

"""
Tcp消息发送
"""


class TcpSendMsg:

    @staticmethod
    def sendMsgStr(channel, str, originalMegId=None, resultType=None):
        msg = TcpMsg()
        msg.originalMegId = originalMegId
        msg.msgType = MsgTypeEnum.Str._value_
        msg.data = str
        TcpSendMsg.sendMsg(channel, msg)

    @staticmethod
    def sendMsgCommand(channel, commands,originalMegId=None):
        msg = TcpMsg()
        msg.msgType = MsgTypeEnum.Command_value_
        msg.originalMegId = originalMegId
        msg.data = commands
        TcpSendMsg.sendMsg(channel, msg)

    @staticmethod
    def sendMsg(channel, msg):
        if msg.id is None : msg.id = uuid.uuid1()
        msg.timeStamp = time.time()
        byte_ = objToByts(msg)
        byte_data = b64encode(byte_)
        channel.send(byte_data)  # 返回信息
