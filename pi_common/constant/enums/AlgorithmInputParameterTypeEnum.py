# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
算法输入参数类型枚举
"""


@unique
class AlgorithmInputParameterTypeEnum(Enum):
    FLOAT = 'float'
    BOOL = 'bool'
    INT = 'int'
    STRING = 'String'
