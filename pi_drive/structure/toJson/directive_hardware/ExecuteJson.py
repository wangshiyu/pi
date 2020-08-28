# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson
from pi_common.util.SerializeUtil import listDictToListObj

"""
驱动执行方式Json
(集合嵌套字典结构)
结构：---》
[
    {
        "queueName": "Car_Directive_Left",
        "executeType": 0
    },
    {
        "queueName": "Car_Directive_Right",
        "executeType": 0
    }
]
"""
class ExecuteJson(BaseJson):
    data = None

    def __init__(self):
        self.data = list()

    def addTriggerTask(self, executeStruc):
        self.data.append(executeStruc)

    def jsonToObj(self, jsonStr):
        list_ = super().jsonToObj(jsonStr)
        obj = listDictToListObj(list_, ExecuteStruc)
        return obj




class ExecuteStruc:
    executeType = None # 执行类型 0 task_queue ,1 thread_pool ，2 direct_run
    queueName = None

