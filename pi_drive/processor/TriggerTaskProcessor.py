# encoding: utf-8
# !/usr/bin/python
from pi_drive.structure.toJson.trgger_info.TriggerTaskJson import TriggerTaskJson
from pi_common.constant.DictKeyConstant import *
from pi_common.util.ReflexUtil import ReflexUtil
from pi_common.component.thread_pool.FuturesThreadPool import FuturesThreadPool
from pi_common.component.thread_pool.FuturesTask import FuturesTask
from pi_common.constant.enums.LoadTypeEnum import LoadTypeEnum
from pi_common.config.Config import Config, ConfigEnum, ConfigValueEnum
from pi_common.constant.enums.TriggerTaskEnum import TriggerTaskExampleEnum
from pi_common.util.structure.Map import Map
from pi_drive.cache.DriveCache import taskIdTotriggerTaskMap

triggerTaskExampleMap = Map()
triggerTaskJson = TriggerTaskJson()
futuresThreadPool = FuturesThreadPool(10)
"""
触发任务处理器
"""


class TriggerTaskProcessor:

    @staticmethod
    def getTriggerTaskDataJson(json):
        return triggerTaskJson.jsonToObj(json)

    @staticmethod
    def triggerTaskBuild(triggerInfo, parametersDict):
        if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.server):
            if triggerInfo.loadType != LoadTypeEnum.Server.value:
                return
        elif Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
            if triggerInfo.loadType != LoadTypeEnum.Client.value:
                return
        triggerTaskJson = TriggerTaskProcessor.getTriggerTaskDataJson(triggerInfo.triggerTaskJson)
        key = triggerTaskJson.triggerTaskClass
        triggerTaskExample = triggerTaskExampleMap.get(key)
        if triggerTaskExample is None:
            triggerTaskExample = TriggerTaskExampleEnum.get(triggerTaskJson.triggerTaskClass)
            if triggerTaskExample is None:
                triggerTaskExample = ReflexUtil.modelGetExample(triggerTaskJson.triggerTaskModel,
                                                         triggerTaskJson.triggerTaskClass)
            triggerTaskExampleMap.put(key, triggerTaskExample)
            print("load triggerTask :" + triggerTaskJson.triggerTaskModel)
        parametersDict[DictKeyConstant.TRIGGER_TASK_ID] = triggerInfo.triggerTaskId
        parametersDict[DictKeyConstant.TRIGGER_TASK_PARAMETERS] = triggerTaskJson.parameters
        triggerTaskExample.addTask(parametersDict)
        taskIdTotriggerTaskMap.put(triggerInfo.triggerTaskId,triggerTaskExample)
        print("add Task :" + str(parametersDict))


class TriggerTaskStart(FuturesTask):

    @staticmethod
    def triggerTaskStart():
        if not triggerTaskExampleMap.isEmpty():
            for triggerTaskExample in triggerTaskExampleMap.values():
                dict = {}
                dict['triggerTaskExample'] = triggerTaskExample
                futuresTask = TriggerTaskStart(dict)
                futuresThreadPool.submitTask(futuresTask)

    def execute(self, dict):
        triggerTask = dict.get('triggerTask')
        if triggerTask is not None:
            triggerTask.start()
