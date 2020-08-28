# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson
from pi_common.util.SerializeUtil import listDictToListObj

"""
驱动执行Json
(集合嵌套字典结构)
结构：---》
[
    {
        "algorithmId": 1,
        "algorithmSign": "L298N",
        "parameters": {
            "CAE_MOVE_DRIVING_TIME": 0.05,
            "CODE_MAPPING_COMPLETE": "#?|#df=false",
            "EXECUTE_QUEUE_ENAME": "Car_Directive_Left",
            "METHOD": "left",
            "RULER_Y": "#&=ruler_yl|#df=1",
            "Y": "#&=yl|#df=0"
        }
    },
    {
        "algorithmId": 1,
        "algorithmSign": "L298N",
        "parameters": {
            "CAE_MOVE_DRIVING_TIME": 0.05,
            "CODE_MAPPING_COMPLETE": "#?|#df=false",
            "EXECUTE_QUEUE_ENAME": "Car_Directive_Right",
            "METHOD": "right",
            "RULER_Y": "#&=ruler_yr|#df=1",
            "Y": "#&=yr|#df=0"
        }
    }
]

注释：#? 以当前key映射
#&=* 以* 映射
#df=* 以*为默认值 
"""




class DirectiveCommadAlgorithmJson(BaseJson):
    data = None

    def __init__(self):
        self.data = list()

    def addTriggerTask(self, directiveCommadAlgorithmStruc):
        self.data.append(directiveCommadAlgorithmStruc)

    def jsonToObj(self, jsonStr):
        list_ = super().jsonToObj(jsonStr)
        obj = listDictToListObj(list_, DirectiveCommadAlgorithmStruc)
        return obj


class DirectiveCommadAlgorithmStruc:
    algorithmSign = None  # 算法标记
    algorithmId = None  # 算法id
    ### 参数
    parameters = None  ## 算法参数dict

# directiveCommadAlgorithmJson = DirectiveCommadAlgorithmJson()
# directiveCommadAlgorithmStruc = DirectiveCommadAlgorithmStruc()
# directiveCommadAlgorithmStruc.algorithmSign='L298N'
# directiveCommadAlgorithmStruc.algorithmId =1
# dict={}
# dict['CAE_MOVE_DRIVING_TIME'] = 0.05
# dict['METHOD'] = 'left'
# dict['CODE_MAPPING_COMPLETE'] = '#?|#df=false'
# dict['Y'] = '#&=yl|#df=0'
# dict['RULER_Y'] = '#&=ruler_yl|#df=1'
# dict['EXECUTE_QUEUE_ENAME'] = 'Car_Directive_Left'
#
# directiveCommadAlgorithmStruc.parameters=dict
# directiveCommadAlgorithmJson.addTriggerTask(directiveCommadAlgorithmStruc)
# directiveCommadAlgorithmStruc = DirectiveCommadAlgorithmStruc()
# directiveCommadAlgorithmStruc.algorithmSign='L298N'
# directiveCommadAlgorithmStruc.algorithmId =1
# dict={}
# dict['CAE_MOVE_DRIVING_TIME'] = 0.05
# dict['METHOD'] = 'right'
# dict['CODE_MAPPING_COMPLETE'] = '#?|#df=false'
# dict['Y'] = '#&=yr|#df=0'
# dict['RULER_Y'] = '#&=ruler_yr|#df=1'
# dict['EXECUTE_QUEUE_ENAME'] = 'Car_Directive_Right'
# directiveCommadAlgorithmStruc.parameters=dict
# directiveCommadAlgorithmJson.addTriggerTask(directiveCommadAlgorithmStruc)
#
# print(directiveCommadAlgorithmJson.toJson())
# directiveCommadAlgorithmJson.jsonToObj(directiveCommadAlgorithmJson.toJson())