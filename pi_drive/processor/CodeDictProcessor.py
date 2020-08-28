# encoding: utf-8
# !/usr/bin/python
from pi_common.constant.AlgorithmConstant import *
from pi_drive.structure.toJson.directive_info.ImportCodeJson import ImportCodeJson
from pi_drive.structure.toJson.directive_info.MethodJson import MethodJson

importCodeJson = ImportCodeJson()
methodJson = MethodJson()

"""
code字典处理器
"""


class CodeDictProcessor:

    @staticmethod
    def getCodeDict(directiveInfo):
        codeDict = {}
        codeDict[AlgorithmConstant.IMPORT_CODES] = importCodeJson.jsonToObj(directiveInfo.importCodeJson)
        methodJsonStr = directiveInfo.methodJson
        methodJsonStr = methodJsonStr.replace('\'', '\"')
        codeDict[AlgorithmConstant.MODELAR] = methodJson.jsonToObj(methodJsonStr)
        codeDict[AlgorithmConstant.CLASS] = directiveInfo.className
        codeDict[AlgorithmConstant.METHOD] = directiveInfo.modularName
        codeDict[AlgorithmConstant.INIT_CODE] = directiveInfo.initCode
        codeDict[AlgorithmConstant.OTHER_CODE] = directiveInfo.otherCode
        return codeDict
