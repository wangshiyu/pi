# encoding: utf-8
# !/usr/bin/python3
from pi_common.constant.enums.CommandTypeEnum import CommandTypeEnum
from pi_server.core.execute_processor.CommandDistribution import DirectiveCommandDistribution, \
    ParameterSynchronizationCommandDistribution
from pi_common.communication.tcp.tcp_Interface.ExecuteSelector import ExecuteSelector
from pi_common.constant.DictKeyConstant import DictKeyConstant

"""
指令选择器
"""


class ServerExecuteSelector(ExecuteSelector):
    directiveCommandDistribution = DirectiveCommandDistribution()

    def addMsg(self, dict):
        commands = dict.get(DictKeyConstant.COMMANDS)
        address = dict.get(DictKeyConstant.ADDRESS)
        if (commands != None and len(commands) != 0):
            for command in commands:
                command.address = address
                if command.commandType is None:
                    pass
                elif CommandTypeEnum.pi_directive._value_ == command.commandType:
                    self.directiveCommandDistribution.distributiond(command)
                elif CommandTypeEnum.pi_parameter_synchronization._value_ == command.commandType:
                    ParameterSynchronizationCommandDistribution.distributiond(command)
                elif CommandTypeEnum.pi_system._value_ == command.commandType:
                    pass
                elif CommandTypeEnum.pi_auth._value_ == command.commandType:
                    pass
        else:
            pass
