# encoding: utf-8
# !/usr/bin/python3
from pi_common.config.Config import Config, ConfigEnum, ConfigValueEnum
from pi_drive.cache.DriveCache import *
from pi_drive.processor.CoreProcessor import CoreProcessor
from pi_common.constant.DictKeyConstant import DictKeyConstant

"""
基础触发任务
"""


class BaseTriggerTask:
    # 触发
    def addTask(self, dict):
        pass

    # 具体的业务逻辑
    def execute(self, dict):
        commands = CoreProcessor.execute(dict)
        dictData = {}
        dictData[DictKeyConstant.ADDRESSS] = dict.get(DictKeyConstant.ADDRESSS)
        dictData[DictKeyConstant.COMMANDS] = commands
        self.addDictData(dictData)

    # 添加或者发送command
    def addDictData(self, dictData):
        getTriggerTaskCommandHandle().addDictData(dictData)
        # if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.server):
        #     triggerTaskCommandHandle.addCommand(dictData)
        # elif Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
        #     triggerTaskCommandHandle.addCommand(dictData)
        # else:
        #     pass

    def removeTask(self,task):
        pass

    def start(self):
        pass

    def close(self):
        pass
