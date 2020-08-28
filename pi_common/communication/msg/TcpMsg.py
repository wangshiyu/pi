# encoding: utf-8
# !/usr/bin/python3
from pi_common.communication.msg.Msg import Msg


"""
TCP通讯实体
"""


class TcpMsg(Msg):
    # originalMsgId = None  # 原消息id
    msgType = None  # 消息类型
    # return_ = False  # 消息是否返
