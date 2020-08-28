# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson
from pi_common.util.SerializeUtil import listDictToListObj

"""
参数映射
结构：---》
{   
    "parametersHandleStrategy":"LAST_IDENTICAL_REFUSE",
    "addresss": "#?",
    "modularIdentification": "#?|#df=L298N_1",
    "algorithmSign": "#?|#df=L298N",
    "ruler_yl": "#?|#df=1.0",
    "ruler_yr": "#?|#df=1.0",
    "yl": "#?|#df=0.0",
    "yr": "#?|#df=0.0"
}

"""


# parametersHandleStrategy 参数处理策略 参考 ParametersHandleStrategyEnum 枚举
# addresss 请求地址
# modularIdentification 模块标识
# algorithmSign 算法标识


class ParametersMappingJson(BaseJson):

    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

# parametersMappingJson = ParametersMappingJson()
# parametersMappingJson.add("ruler_yl","#?|#df=1.0")
# parametersMappingJson.add("ruler_yr","#?|#df=1.0")
# parametersMappingJson.add("yl","#?|#df=0.0")
# parametersMappingJson.add("yr","#?|#df=0.0")
# parametersMappingJson.add("ruler_yl","#?|#df=1.0")
# parametersMappingJson.add("modularIdentification","#?|#df=L298N_1")
# parametersMappingJson.add("addresss","#?")
#
# print(parametersMappingJson.toJson())
