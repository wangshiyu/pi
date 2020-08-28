# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
消息类型
"""


@unique
class MsgTypeEnum(Enum):
    Command = 'Command'  # 命令类型
    Result = 'Result'  # 返回类型
    Str = 'Str'  # 字符串
    JsonStr = 'JsonStr'  # json字符串
