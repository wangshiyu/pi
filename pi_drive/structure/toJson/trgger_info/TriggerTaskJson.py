# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson
from pi_common.util.SerializeUtil import dictToObj

"""
触发器任务Json
(集合嵌套字典结构)
结构：---》
{
    "parameters": [
        5
    ],
    "triggerTaskClass": "MsecTriggerTask",
    "triggerTaskModel": "pi_drive.task.MsecTriggerTask"
}
"""


class TriggerTaskJson(BaseJson):
    data = None

    def __init__(self):
        self.data = {}

    def addTriggerTask(self, triggerTaskStruc):
        self.data = triggerTaskStruc.__dict__

    def jsonToObj(self, jsonStr):
        dict = super().jsonToObj(jsonStr)
        return dictToObj(dict,TriggerTaskStruc)


class TriggerTaskStruc:
    triggerTaskModel = None  # 触发模块
    triggerTaskClass = None  # 触发类
    ### 参数
    parameters = None  ## 触发任务参数集合


# triggerTaskJson = TriggerTaskJson()
# triggerTaskStruc = TriggerTaskStruc()
# triggerTaskStruc.triggerTaskModel = 'pi_drive.task.MsecTriggerTask'
# triggerTaskStruc.triggerTaskClass = 'MsecTriggerTask'
# triggerTaskStruc.parameters = [0.05]
# triggerTaskJson.addTriggerTask(triggerTaskStruc)
# print(triggerTaskJson.toJson())
# triggerTaskJson.jsonToObj(triggerTaskJson.toJson())
