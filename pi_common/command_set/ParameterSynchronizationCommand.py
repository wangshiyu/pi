# encoding: utf-8
# !/usr/bin/python3
from pi_common.command_set.Command import Command

"""
参数同步指令
"""


class ParameterSynchronizationCommand(Command):
    parameterSynchronizationType = None  # 参数同步类型
    key = None
    value = None