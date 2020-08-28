# encoding: utf-8
# !/usr/bin/python3
from pi_drive.cache.StructureJsonCache import parametersMappingJsonMap
from pi_common.exception.PiException import NotConfiguredException
from pi_common.analysis.ParameterAnalysis import ParameterAnalysis
from pi_client.core.handle.ParameterSynchronizationTask import ParameterSynchronizationTask
from pi_client.cache.ClientCoreCache import parameterSynchronizationTaskQueue
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_drive.cache.DriveCache import directiveParameterMap, taskIdTotriggerTaskMap, \
    directiveCommadAlgorithmLoadType, modularToTaskId
from pi_common.util.DictUtil import dictCopy
from pi_client.core.handle.ParametersHandleStrategyHandle import ParametersHandleStrategyHandle
from pi_drive.task.ExternalTriggerTask import ExternalTriggerTask

"""
统一操控参数控制

"""


class ManipulationParametersControl:

    @staticmethod
    def addTo(data):
        modularIdentification = data.get(DictKeyConstant.MODULAR_IDENTIFICATION)
        if modularIdentification is None:
            raise NotConfiguredException('==>modularIdentification not configured!')
        parametersMapping = parametersMappingJsonMap.get(modularIdentification)
        keys = parametersMapping.keys()
        if len(keys) > 0:
            parametersDict = {}
            for key in keys:
                value = parametersMapping.get(key)
                dict = data
                value_ = ParameterAnalysis.mapping(key, value, dict)
                parametersDict[key] = value_
            ManipulationParametersControl.parametersHandle(parametersDict)

    """
    参数处理
    """

    @staticmethod
    def parametersHandle(parametersDict):
        if ParametersHandleStrategyHandle.filter(parametersDict):
            return False
        if directiveCommadAlgorithmLoadType.get(
                DictKeyConstant.ALGORITHM_SIGN + DictKeyConstant.CLIENT_SUFFIX) is True:  # 同步
            task = ParameterSynchronizationTask()
            task.key = parametersDict.get(DictKeyConstant.MODULAR_IDENTIFICATION)
            task.value = parametersDict
            task.addresss = parametersDict.get(DictKeyConstant.ADDRESSS)
            parameterSynchronizationTaskQueue.add(task)
        else:
            modularIdentification = parametersDict.get(DictKeyConstant.MODULAR_IDENTIFICATION)
            dict = directiveParameterMap.get(modularIdentification)
            dictCopy(parametersDict, dict)  # 数据拷贝
            taskId = modularToTaskId.get(modularIdentification)
            externalTriggerTask = taskIdTotriggerTaskMap.get(taskId)
            if type(externalTriggerTask) == type(ExternalTriggerTask()):  ## 如果是外部执行任务，直接执行
                externalTriggerTask.execute(parametersDict)
