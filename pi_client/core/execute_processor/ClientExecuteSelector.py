# encoding: utf-8
# !/usr/bin/python3
from pi_common.constant.enums.CommandTypeEnum import CommandTypeEnum
from pi_common.constant.enums.ResultTypeEnum import ResultTypeEnum
from pi_common.communication.tcp.tcp_Interface.ExecuteSelector import ExecuteSelector
from pi_common.command_set.Result import Result
from pi_common.command_set.Command import Command
from pi_client.cache.PiClientCache import codeMappingCompleteMapCache

"""
指令选择器
"""


class ClientExecuteSelector(ExecuteSelector):

    def __init__(self):
        pass

    def addMsg(self, msg, address_str):
        data = msg.data
        if type(data) == Command:
            if data != None and len(data) != 0:
                for command in data:
                    command.address = address_str
                    if command.commandType is None:
                        pass
                    elif CommandTypeEnum.pi_directive._value_ == command.commandType:
                        pass
                    elif CommandTypeEnum.pi_system._value_ == command.commandType:
                        pass
                    elif CommandTypeEnum.pi_auth._value_ == command.commandType:
                        pass
        elif type(data) == Result:
            if data.resultType == ResultTypeEnum.pi_codeMapping:
                falg = codeMappingCompleteMapCache.get(data.date['directiveCommandCode'])
                if falg != True:
                   codeMappingCompleteMapCache.put(data.date['directiveCommandCode'], True)
                   print('驱动代码映射完成')
        else:
            pass
