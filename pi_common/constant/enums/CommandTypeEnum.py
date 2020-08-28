# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
指令类型枚举
"""


@unique
class CommandTypeEnum(Enum):
    pi_auth = 0  # 授权
    pi_system = 1  # 系统
    pi_directive = 2  # 驱动
    pi_parameter_synchronization = 3  # 参数同步


if __name__ == "__main__":
    print( type(CommandTypeEnum.pi_directive._value_))
