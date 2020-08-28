# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson

"""
输入参数JSON
(字典结构)
结构：---》 
{
     "CAE_MOVE_DRIVING_TIME": 'float',
     "CODE_MAPPING_COMPLETE": 'bool',
     "METHOD": 'String',
     "RULER_Y": 'float',
     "Y": 'float'
}
"""


class InputParameterTypeJson(BaseJson):
    data = None

    def __init__(self):
        self.data = {}

    def addChanne(self, key, value):
        self.data[key] = value
