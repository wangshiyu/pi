# encoding: utf-8
# !/usr/bin/python
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_db.common.dao.DirectiveCommadAlgorithmDao import DirectiveCommadAlgorithmDao
from pi_drive.cache.StructureJsonCache import inputParameterTypeJsonMap
from pi_drive.structure.toJson.directive_hardware.DirectiveCommadAlgorithmJson import DirectiveCommadAlgorithmJson
from pi_common.analysis.ParameterAnalysis import ParameterAnalysis
from pi_common.analysis.ParameterTypeChange import ParameterTypeChange

"""
驱动算法参数字典处理器
"""
directiveCommadAlgorithmJson = DirectiveCommadAlgorithmJson()
directiveCommadAlgorithmDao = DirectiveCommadAlgorithmDao()


class DirectiveCommadAlgorithmParametersDictProcessor:

    @staticmethod
    def getDirectiveCommadAlgorithmJson(json):
        return directiveCommadAlgorithmJson.jsonToObj(json)

    @staticmethod
    def getParamsDict(directiveCommadAlgorithmList, dict):
        directiveCommadAlgorithmDict = {}
        for item in directiveCommadAlgorithmList:
            if item.algorithmSign is None or '':
                raise RuntimeError('algorithmSign is None! modular identification is:' + dict.get(
                    DictKeyConstant.MODULAR_IDENTIFICATION))
            if item.algorithmId is None or '':
                raise RuntimeError('algorithmId is None! modular identification is:' + dict.get(
                    DictKeyConstant.MODULAR_IDENTIFICATION))
            paramsLsit = None
            if directiveCommadAlgorithmDict.get(item.algorithmSign) is not None:
                paramsLsit = directiveCommadAlgorithmDict.get(item.algorithmSign)
            else:
                paramsLsit = list()
                directiveCommadAlgorithmDict[item.algorithmSign] = paramsLsit
            inputParameterTypeDict = inputParameterTypeJsonMap.get(item.algorithmSign)
            paramsDict = {}
            parameterDict = item.parameters
            for key in parameterDict.keys():
                value = ParameterAnalysis.mapping(key.strip(), parameterDict.get(key), dict)
                paramsDict[key] = ParameterTypeChange.valueTypeFormat(key, value, inputParameterTypeDict.get(key))
            paramsLsit.append(paramsDict)
        return directiveCommadAlgorithmDict

