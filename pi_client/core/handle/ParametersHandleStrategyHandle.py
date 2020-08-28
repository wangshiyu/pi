# encoding: utf-8
# !/usr/bin/python3
from pi_common.constant.enums.ParametersHandleStrategyEnum import ParametersHandleStrategyEnum
from pi_common.util.structure.Map import Map
from pi_common.constant.DictKeyConstant import DictKeyConstant
import random

"""
参数处理策略 处理

"""
parametersoOldMap = Map()


class ParametersHandleStrategyHandle:
    pass

    """
    过滤
    """
    @staticmethod
    def filter(parametersDict):
        parametersHandleStrategy = parametersDict.get(DictKeyConstant.PARAMETERS_HANDLE_STRATEGY)
        modularIdentification = parametersDict.get(DictKeyConstant.MODULAR_IDENTIFICATION)

        if parametersHandleStrategy is None \
                or parametersHandleStrategy == ParametersHandleStrategyEnum.ALL_ADOPT.value:
            return False
        elif parametersHandleStrategy == ParametersHandleStrategyEnum.ALL_REFUSE.value:
            return True
        elif parametersHandleStrategy == ParametersHandleStrategyEnum.RANDOM.value:
            i = random.randint(0, 9)
            if i % 2 == 0: return True  ## 随机丢弃
        elif parametersHandleStrategy == ParametersHandleStrategyEnum.Last_Identical_Refuse.value:
            oldDict = parametersoOldMap.get(modularIdentification)
            parametersoOldMap.put(modularIdentification, parametersDict)
            return ParametersHandleStrategyHandle.validate(oldDict, parametersDict)
        return False

    """
   参数验证 ,判断是否和之前参数相同
   """
    @staticmethod
    def validate(oldDate, newDate):
        if oldDate is None or newDate is None:
            return False
        keys1 = newDate.keys()
        keys2 = oldDate.keys()
        if len(keys1) != len(keys2):
            return False
        elif len(keys1) == len(keys2) == 0:
            return False
        else:
            for key in keys1:
                if (newDate.get(key) != oldDate.get(key)):
                    return False
        return True
