# encoding: utf-8
# !/usr/bin/python3
from pi_server.cache.PiServerCache import codeMappingMapCache,tcpServiceChannelMapCache
from pi_server.core.execute_handle.DirectiveExecuteHandle import DirectiveExecuteHandle
from pi_server.cache.cache_entity.CodeMapping import CodeMapping
from pi_common.communication.tcp.server.TcpSocketServiceMsgSend import TcpSocketServiceMsgSend
from pi_common.constant.enums.ResultTypeEnum import ResultTypeEnum
from pi_common.component.task_queue.TaskQueueExecute import TaskQueueExecute
from pi_common.component.thread_pool.FuturesTask import FuturesTask
import time
from pi_common.constant.DictKeyConstant import *

"""
驱动命令处理器
"""


class DirectiveExecuteProcessor(TaskQueueExecute):

    """
    执行
    """

    def execute(self, dict):
        command = dict.get(DictKeyConstant.COMMAND)
        DirectiveExecuteProcessor.commandExecute(command)

    """
    执行命令
    """

    @staticmethod
    def commandExecute(command):
        codeStr = DirectiveExecuteProcessor.gitCodeStr(command)
        DirectiveExecuteHandle.execute_method_codeMapping(codeStr, command.parameter)

    """
    获得代码
    """

    @staticmethod
    def gitCodeStr(command):
        directiveCommandCode = command.directiveCommandCode
        if codeMappingMapCache.get(directiveCommandCode) is not None:
            if command.className != None or command.methodName != None or command.otherCode != None:  # 如果代码已经缓存 同步状态
                tcpchabbe = tcpServiceChannelMapCache.get(command.address)
                if tcpchabbe != None:
                    TcpSocketServiceMsgSend.sendResultMsg(tcpchabbe.channel,
                                                          {"directiveCommandCode": directiveCommandCode}, command.id,
                                                          ResultTypeEnum.pi_codeMapping)  # 通知映射成功
            codeMapping = codeMappingMapCache.get(directiveCommandCode)
            codeMapping.invokingTime = time.time()
            codeMapping.invokingSize += 1
            return codeMapping.codeStr
        else:
            codeStr = DirectiveExecuteProcessor.structureCodeStr(command)
            if (codeStr is None):
                pass  # 需要反馈消息为空
            codeMappingMapCache.put(command.directiveCommandCode, CodeMapping(directiveCommandCode, codeStr))
            return codeStr

    """
    构建代码
    """

    @staticmethod
    def structureCodeStr(command):
        return DirectiveExecuteHandle.buildCodeStr(command.importCodes, command.initCode, command.modularName,
                                                   command.className, command.methodName, command.otherCode)
