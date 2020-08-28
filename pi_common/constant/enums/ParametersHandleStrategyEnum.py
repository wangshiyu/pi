# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
参数处理策略
"""


@unique
class ParametersHandleStrategyEnum(Enum):
    ALL_ADOPT = 'ALL_ADOPT'  # 所有通过 (默认值)
    ALL_REFUSE = 'ALL_REFUSE'  # 所有拒绝
    RANDOM = 'RANDOM'  # 随机
    Last_Identical_Refuse = 'LAST_IDENTICAL_REFUSE'  # 上一条相同的拒绝
