# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
驱动模式
"""


@unique
class PatternTypeEnum(Enum):
    RUNING = 0  # 运行模式
    TEST = 1  # 测试模式
