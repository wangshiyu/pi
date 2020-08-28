# encoding: utf-8
# !/usr/bin/python3

"""
ajax 返回结果
"""


class AjaxResult:
    status = None  # 状态  Success，Fail
    data = None

    def __init__(self, status, data):
        self.status = status
        self.data = data

    def toDicJson(self):
        dic = {}
        dic['status'] = self.status
        try:
            dic['data'] = self.data.toDict()
        except Exception:
            dic['data'] = self.data
        return dic

    @staticmethod
    def buildFailAjaxResult(data=None):
        return AjaxResult("Fail", data).toDicJson()

    @staticmethod
    def buildSuccessAjaxResult(data=None):
        return AjaxResult("Success", data).toDicJson()
