# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
驱动类型枚举
"""

@unique
class DirectiveTypeEnum(Enum):
    Car_Directive_Left = "Car_Directive_Left"   # 左电机
    Car_Directive_Right = "Car_Directive_Right"  # 右电机
