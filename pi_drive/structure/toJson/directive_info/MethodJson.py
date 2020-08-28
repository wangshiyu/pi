# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson
from pi_common.util.SerializeUtil import listDictToListObj

"""
方法json
(集合嵌套字典结构)
结构：---》
[
    {
        "name": "left",
        "parameter": [
            "functionType",
            "sleep_time1",
            "sleep_time2"
        ]
    },
    {
        "name": "right",
        "parameter": [
            "functionType",
            "sleep_time1",
            "sleep_time2"
        ]
    }
]

"""


class MethodJson(BaseJson):
    data = None

    def __init__(self):
        self.data = list()

    def addMethod(self, name, parameter):
        method = MethodStruc()
        method.name = name
        method.parameter = parameter
        self.data.append(method)

    def jsonToObj(self, jsonStr):
        list_ = super().jsonToObj(jsonStr)
        objList = listDictToListObj(list_, MethodStruc)
        return objList


"""
方法结构
"""


class MethodStruc:
    name = None
    parameter = None


# methodJson = MethodJson()
# methodJson.addMethod('left', ["functionType", "sleep_time1", "sleep_time2"])
# methodJson.addMethod('right', ["functionType", "sleep_time1", "sleep_time2"])
# print(methodJson.toJson())
# list_ = methodJson.jsonToObj(methodJson.toJson())
# print(list_)

