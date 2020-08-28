# encoding: utf-8
# !/usr/bin/python3
from pi_common.command_set.Command import Command

"""
驱动指令实体
所有驱动命令必须绑定到队列上
"""


class DirectiveCommand(Command):
    directiveCommandCode = None  # 驱动指令 对应的别名 通过与代码映射，减少代码数据的传输
    importCodes = None  # 导入代码
    initCode = None  # 初始化代码
    modularName = None  # 模块名称
    className = None  # 类名称
    methodName = None  # 方法名称
    parameter = None  # 请求参数
    otherCode = None  # 其他代码
    queueName = None  # 队列名称 通过命令队列控制每个驱动，实现并行
    interruptionTime = None  # 中断时间 （ms）当前命令中断多长执行下一条命令

    def __init__(self):
        pass
