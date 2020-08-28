# encoding: utf-8
# !/usr/bin/python3
import json

"""
基础json
"""


class BaseJson:
    data = None

    def toJson(self):
        JsonStr = json.dumps(self.data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return JsonStr

    def jsonToObj(self, jsonStr):
        return json.loads(jsonStr)
