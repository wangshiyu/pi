# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
参数同步类型
"""


@unique
class ParameterSynchronizationTypeEnum(Enum):
    SYSTEM = 0  # 系统参数同步
    DIRECTIVE = 1  # 驱动参数同步
    DB = 2  # 数据库同步
