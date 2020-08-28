# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
加载类型
"""


@unique
class LoadTypeEnum(Enum):
    Server = 1  # 服务端加载
    Client = 2  # 客户端加载
