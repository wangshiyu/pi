# encoding: utf-8
# !/usr/bin/python3

"""
服务端数据发送封装类
"""
from pi_common.communication.msg.TcpMsg import TcpMsg
from pi_common.constant.enums.MsgTypeEnum import MsgTypeEnum
import uuid
from pi_common.util.Base64Util import b64encode
from pi_common.util.SerializeUtil import objToByts
from pi_common.command_set.Result import Result
import time


class TcpSocketServiceMsgSend:

    @staticmethod
    def sendMsgStr(channel, str, msgType=MsgTypeEnum.Str):
        msg = TcpMsg()
        msg.timeStamp = time.time()
        msg.msgType = msgType
        msg.data = str
        TcpSocketServiceMsgSend.sendMsg(channel, msg)

    @staticmethod
    def sendMsg(channel, msg):
        msg.id = uuid.uuid1()
        byte_ = objToByts(msg)
        byte_data = b64encode(byte_)
        channel.send(byte_data)  # 返回信息

    @staticmethod
    def sendResultMsg(channel, dic, commandId=None, resultType=None, msgType=MsgTypeEnum.Result):
        msg = TcpMsg()
        msg.timeStamp = time.time()
        msg.msgType = msgType
        msg.data = Result()
        msg.data.id = uuid.uuid1()
        msg.data.commandId = commandId
        msg.data.resultType = resultType
        msg.data.data = dic
        TcpSocketServiceMsgSend.sendMsg(channel, msg)
