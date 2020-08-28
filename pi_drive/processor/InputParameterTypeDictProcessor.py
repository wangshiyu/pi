# encoding: utf-8
# !/usr/bin/python
from pi_drive.structure.toJson.directive_commad_algorithm.InputParameterTypeJson import InputParameterTypeJson

inputParameterTypeJson = InputParameterTypeJson()

"""
输入参数类型字典处理器
"""


class InputParameterTypeDictProcessor:

    @staticmethod
    def getInputParameterTypeJSON(json):
        return inputParameterTypeJson.jsonToObj(json)
