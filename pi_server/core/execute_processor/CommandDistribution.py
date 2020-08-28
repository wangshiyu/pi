# encoding: utf-8
# !/usr/bin/python3

from pi_server.core.execute_processor.DirectiveExecuteProcessor import DirectiveExecuteProcessor
from pi_common.component.task_queue.TaskQueue import TaskQueue
from pi_server.cache.PiServerCache import directiveCommandMapCache
from pi_common.component.thread_pool.FuturesThreadPool import FuturesThreadPool
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_common.constant.enums.ParameterSynchronizationTypeEnum import ParameterSynchronizationTypeEnum
from pi_server.core.execute_processor.parameter_synchronization.DirectiveParameterSynchronizationProcessor import DirectiveParameterSynchronizationProcessor

"""
驱动命令分发
"""


class DirectiveCommandDistribution:
    futuresThreadPool = None

    def distributiond(self, command):
        if command is None: return
        if command.queueName != None:
            queueName = str(command.queueName)
            directiveCommandQueueData = directiveCommandMapCache.get(queueName)
            if directiveCommandQueueData is None:
                directiveCommandQueueData = TaskQueue(queueName, DirectiveExecuteProcessor())
                directiveCommandMapCache.put(queueName, directiveCommandQueueData)
            dictDate={}
            dictDate[DictKeyConstant.COMMAND]=command
            directiveCommandQueueData.add(dictDate)
        else:
            if self.futuresThreadPool is None:
                self.futuresThreadPool = FuturesThreadPool(100)
            dict = {}
            dict[DictKeyConstant.COMMAND] = command
            if command.return_ == True:
                result = self.futuresThreadPool.submitTaskResult(DirectiveExecuteProcessor(dict))
                pass  # 消息返回出去 或者在任务执行的时候返回
            else:
                self.futuresThreadPool.submitTask(DirectiveExecuteProcessor(dict))


"""
参数同步命令分发
"""


class ParameterSynchronizationCommandDistribution:
    @staticmethod
    def distributiond(command):
        if command is None: return
        if command.parameterSynchronizationType == ParameterSynchronizationTypeEnum.DIRECTIVE.value:
            DirectiveParameterSynchronizationProcessor.doHandle(command)
        elif command.parameterSynchronizationType == ParameterSynchronizationTypeEnum.SYSTEM.value:
            pass
        elif command.parameterSynchronizationType == ParameterSynchronizationTypeEnum.DB.value:
            pass


